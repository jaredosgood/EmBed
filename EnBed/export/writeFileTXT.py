
import os

def write_file(file_path: str, text: str) -> None:
    mode = 'a' if os.path.exists(file_path) else 'w'
    try:
        with open(file_path, mode) as file:
            file.write(text)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Cannot write to file: {str(e)}")