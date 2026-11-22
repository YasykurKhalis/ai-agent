import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run or execute the python file in a specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Python file path to run, relative to the working directory",
                },
                "args": {
                    "type": "list",
                    "description": "Argument to pass to the executable python file, can be None",
                },
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not absolute_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        if args != None:
            command.extend(args)
        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}" "\n"
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += "STDOUT:" + "\n" + result.stdout
            if result.stderr:
                output += "STDERR:" + "\n" + result.stderr
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"