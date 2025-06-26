import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_TRIES, MODEL
from prompts import SYSTEM_PROMPT
from functions.call_function import call_function, available_functions


def main():
    load_dotenv()

    is_verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("Uso: python main.py <user_prompt> [--verbose]")
        print(
            "Exemplo: python main.py 'Como eu construo um app de calculadora?' --verbose"
        )
        sys.exit(1)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_content(client, messages, is_verbose)


def generate_content(client, messages, is_verbose):
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[available_functions],
    )

    for i in range(0, MAX_TRIES):
        response = client.models.generate_content(
            model=MODEL, contents=messages, config=config
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if is_verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        if not response.function_calls:
            print(response.text)
            break

        function_responses = []
        for function_call in response.function_calls:
            result = call_function(function_call, is_verbose)
            if not result.parts or not result.parts[0].function_response:
                raise Exception("empty function call result")
            if is_verbose:
                print(f"-> {result.parts[0].function_response.response}")
            messages.append(result)
            function_responses.append(result.parts[0])

        if not function_responses:
            raise Exception("Sem nenhum resultado de função retornado.")

    if is_verbose:
        print(f"{i + 1} interações realizadas.")


if __name__ == "__main__":
    main()
else:
    print("Esse script deve ser executado diretamente.")
    sys.exit(1)
