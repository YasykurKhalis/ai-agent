import os
from functions.working_dir_abs import working_dir_abs

def write_file(working_directory: str, file_path: str, content: str) -> str:
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(target_file):
        return print(f'Error: Cannot write to "{file_path}" as it is a directory')

    # print((target_file.rsplit("/",1))[0])
    os.makedirs((target_file.rsplit("/",1))[0], mode=0o777, exist_ok=True)

    f = open(target_file,"w")
    f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'