from EnBed.logging_config import setup_logging
import logging
import os

def generate_unique_filename(directory: str, base_name: str, max_attempts: int = 10000) -> str:
    """
    Generate a unique filename, with a limit on the number of attempts to avoid possible infinite loop
    """
    counter = 1
    while counter <= max_attempts:
        new_name = f"{base_name}_{counter}.txt"
        new_path = os.path.join(directory, new_name)
        if not os.path.exists(new_path):
            return new_path
        counter += 1
    raise RuntimeError("Max filename generation attempts reached")

def write_to_file_with_error_handling(file_path: str, base_name: str, text: str) -> str:
    """
    Try to write to a file with error handling, will raise an exception if writing is unsuccessful
    """
    setup_logging()
    logger = logging.getLogger('EnBed.export.write_to_txt_file.write_to_file_with_error_handling')
    try:
        with open(file_path, 'w') as output_file:
            output_file.write(text)
        return file_path
    except (IsADirectoryError, FileNotFoundError, PermissionError) as error:
        logger.error(f"An error occurred while writing to a file: {error}")
        raise

def write_to_txt_file(base_directory: str, base_name: str, text: str) -> None:
    setup_logging()
    logger = logging.getLogger('EnBed.export.write_to_txt_file.write_to_text_file')
    file_path = generate_unique_filename(base_directory, base_name)
    # Attempt to write to the desired location
    try:
        write_to_file_with_error_handling(file_path, base_name, text)
    except Exception:  # If it failed, attempt to write to the fallback location
        # Fallback to Downloads folder
        downloads_path = os.path.expanduser('~/Downloads')
        fallback_path = generate_unique_filename(downloads_path, base_name)
        write_to_file_with_error_handling(fallback_path, base_name, text)
        logger.info(f"Written to fallback location: {fallback_path}")




# Example usage:
# IPSUM_PATH = "/Users/jdo/EnBed/EnBed/test/ipsum_01.txt"
# with open(IPSUM_PATH, "r") as file:
#     text = file.read()
#     write_txt_to_file("/Users/jdo/Desktop/FUCK", text)