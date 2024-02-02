import logging
import os
from EnBed.db_functions.prepare_data_for_db import prepare_data_for_db
from EnBed.logging_config import setup_logging
from EnBed.utilities.retry_on_rate_limit_errors import retry_on_rate_limit_error

setup_logging()
logger = logging.getLogger('EnBed.main')
# PDF_PATH = "/Users/jdo/Library/CloudStorage/OneDrive-Personal/ASU Courses/CSE 230/Computer Organization and Design.pdf"
API_KEY = os.environ.get("OPENAI_API_KEY")
# OUTPUT_FILE_PATH = "/Users/jdo/Library/CloudStorage/OneDrive-Personal/ASU Courses/CSE 230/ComputerOrgAndDesignPunctuated"
# BASE_NAME = "ComputerOrgAndDesign"

def main():
    # Wait for extraction to complete
    # text_extracted_from_pdf = pdf_to_var(PDF_PATH)
    # logger.info(f"'pdf_to_var()' called and text was extracted: {text_extracted_from_pdf[0:124]}\n"
    #             f"{text_extracted_from_pdf[125:250]}\n"
    #             f"{text_extracted_from_pdf[251:375]}\n"
    #             f"{text_extracted_from_pdf[376:500]}\n"
    #             f"..."
    #             f"\n{text_extracted_from_pdf[-100:]}")
    # print(text_extracted_from_pdf)
    # chunks_dict = split_with_overlap(text_extracted_from_pdf, 60, 1000)
    # logger.info(f"'chunks_dict()' called -- Number of chunks: {len(chunks_dict)}")
    # processed_text = process_chunks(chunks_dict)
    # logger.info(f"'processed_text()' called -- Processed text: {processed_text[:1000]}")
    # write_to_txt_file(OUTPUT_FILE_PATH, BASE_NAME, processed_text)
    # logger.info(f"'write_txt_file()' called -- File written to {OUTPUT_FILE_PATH}")
    # logger.info(f"Program ended successfully.")
    retry_on_rate_limit_error(prepare_data_for_db)
    return


if __name__ == '__main__':
    main()


# # Append response to SQLite DB
# append_response_to_db(db_path, table_name, response_data)
#
# # Example usage
# if __name__ == "__main__":
#     db_path = "EnBed/db/EnBed.sqlite"
#     table_name = "corrections"
#     raw_text = "Your text here..."
#     punctuation_assistant(raw_text, db_path, table_name)