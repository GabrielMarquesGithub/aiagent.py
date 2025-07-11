import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
            timeout=30,
        )

        output_lines = []
        if result.stdout:
            output_lines.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output_lines.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")

        # Retorna resultado formatado ou mensagem padrão
        return "\n".join(output_lines) if output_lines else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python file.",
            ),
        },
    ),
)
