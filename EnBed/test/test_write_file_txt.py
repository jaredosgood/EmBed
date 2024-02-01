from EnBed.export.write_to_txt_file import generate_unique_filename, write_to_file_with_error_handling, write_to_txt_file
import os


DOWNLOADS = os.path.expanduser('~/Downloads')
def test_generate_unique_filename():
    print("Running test_generate_unique_filename()")

    # Define a directory where test files will be created (make sure it exists and is writable)
    directory = os.path.expanduser('~/Downloads')  # Adjust to your path
    base_name = "test"

    try:
        # Test for general case
        file_path = generate_unique_filename(directory, base_name)
        print(f"Generated file path: {file_path}")

        # Test for edge case - maximum attempts
        for i in range(10001):  # Try one more than max_attempts
            file_path = generate_unique_filename(directory, f"edge_case")

        print("test_generate_unique_filename() passed")
    except Exception as e:
        print(f"test_generate_unique_filename() failed: {str(e)}")


def test_write_to_file_with_error_handling():
    print("Running test_write_to_file_with_error_handling()")
    file_path = os.path.join(DOWNLOADS, "file.txt")
    base_name = "test"

    try:
        # Test for general case
        write_to_file_with_error_handling(file_path, base_name, "Test string")

        # Test for edge case - directory error
        write_to_file_with_error_handling("/nonexistent_dir/test.txt", base_name, "Test string")

        print("test_write_to_file_with_error_handling() passed")
    except Exception as e:
        print(f"test_write_to_file_with_error_handling() failed: {str(e)}")


def test_write_txt_to_file():
    print("Running test_write_txt_to_file()")

    # Define a directory and base name for testing (make sure directory exists and is writable)
    base_directory = os.path.expanduser('~/Downloads')  # Adjust to your path
    base_name = "test"
    text = "Test string"

    try:
        # Test for general case
        write_to_txt_file(base_directory, base_name, text)

        # Test for edge case - fallback to Downloads folder
        write_to_txt_file("/nonexistent_dir", base_name, text)

        print("test_write_txt_to_file() passed")
    except Exception as e:
        print(f"test_write_txt_to_file() failed: {str(e)}")

# Run the tests
test_generate_unique_filename()
test_write_to_file_with_error_handling()
test_write_txt_to_file()