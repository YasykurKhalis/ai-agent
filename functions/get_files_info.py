import os
from config import MAX_CHARS
from functions.working_dir_abs import working_dir_abs

def get_files_info(working_directory: str, directory: str = ".") -> str:
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(target_dir):
        return print(f'Error: "{directory}" is not a directory')
    print(f'Success: "{directory}" is within the working directory')
    # debugging tips:
    # use try/except block to catch errors raised by standard library functions (yk, if errors didnt come from your own code)

    print("Result for current directory:")
    for item in os.listdir(target_dir):
        print(f'- {item}: file_size={os.path.getsize(os.path.join(target_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, item))}')

def get_file_content(working_directory: str, file_path: str) -> str:
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(target_file):
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    
    f = open(target_file,"r")
    content = f.read(MAX_CHARS)

    if f.read(1):
        content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content