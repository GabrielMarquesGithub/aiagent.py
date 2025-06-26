from google.genai import types

from functions.get_file_content import get_file_content, schema_get_file_contents
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.get_files_info import get_files_info, schema_get_files_info
from config import WORKING_DIR


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_contents,
        schema_write_file,
        schema_run_python_file,
    ]
)


def call_function(function_call, is_verbose):
    function_name = function_call.name

    if is_verbose:
        print(f" - Calling function: {function_name}({function_call.args})")
    else:
        print(f" - Calling function: {function_name}")

    functions = {
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
        "get_files_info": get_files_info,
    }

    if function_name in functions:
        function = functions[function_name]
        result = function(WORKING_DIR, **function_call.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )
