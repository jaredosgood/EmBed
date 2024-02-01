import os
import logging
import pandas as pd
import json
from ext_type import ext_type

# Configure logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def manage_file(file_type, action, OUTPUT_DIR, INPUT):
    """
    A function to handle file operations for different file types.

    Parameters:
    - file_type (str): One of 'txt', 'json', 'csv', 'excel'.
    - action (str): One of 'w', 'r', 'a' for write, read, append.
    - OUTPUT_DIR (str): The output directory path.
    - INPUT: File name (for read action) or content to write/append.

    Returns:
    depends on operation, can be the content of a file for read operation, or None
    """
    file_path = os.path.join(OUTPUT_DIR, f"{INPUT if action == 'r' else 'output'}.{ext_type.ext_type(file_type)}")

    try:
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            logging.info(f"Directory {OUTPUT_DIR} was created.")

        if action == 'r':
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            if file_type in ('txt', 'json'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file) if file_type == 'json' else file.read()
            elif file_type in ('csv', 'excel'):
                return pd.read_excel(file_path) if file_type == 'excel' else pd.read_csv(file_path)

        elif action in ('w', 'a'): # Write or Append
            mode = 'w' if action == 'w' else 'a'
            if file_type == 'txt':
                with open(file_path, f'{mode}t', encoding='utf-8') as file:
                    file.write(INPUT)
            elif file_type == 'json':
                with open(file_path, f'{mode}', encoding='utf-8') as file:
                    json.dump(INPUT, file)
            elif file_type == 'csv':
                pd.DataFrame(INPUT).to_csv(file_path, mode=mode, index=False)
            elif file_type == 'excel':
                pd.DataFrame(INPUT).to_excel(file_path, index=False)

            logging.info(f"File {file_path} has been {'written to' if action == 'w' else 'appended'} successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

    return None
# Example of using the function
# manage_file('txt', 'w', 'path_to_output', 'Hello World!')