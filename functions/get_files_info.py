import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Will be True or False
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