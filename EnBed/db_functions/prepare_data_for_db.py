from EnBed.db_functions.append_response_to_db import append_response_to_db
from EnBed.db_functions.db_ops import find_last_processed_page
from EnBed.process_text.punctuation_assistant import punctuation_assistant
import fitz
from EnBed.utilities.constants import DB_PATH, TABLE_NAME, AUTHOR, BOOK_TITLE, PDF_PATH
from EnBed.utilities.create_guid import create_guid
from EnBed.logging_config import setup_logging
from EnBed.process_text.summarize_textbook_pages_assistant import summarize_textbook_pages_assistant
from EnBed.process_text.get_embedddings import get_embeddings
import logging
from concurrent.futures import ThreadPoolExecutor


db_path = DB_PATH
table_name = TABLE_NAME
author = AUTHOR
book_title = BOOK_TITLE
pdf_path = PDF_PATH

# Set up logging
setup_logging()
logger = logging.getLogger('EnBed.export.pdf_to_df')


# This function gets the text from the page.
def get_text_from_page(doc, start_idx, end_idx):
    text_from_page = ""
    for i in range(start_idx, min(end_idx, len(doc))):
        page = doc.load_page(i)
        text_from_page += page.get_text().encode("utf8").decode("utf8") + "\f"
    return text_from_page


# This function prepares the data for the database.
def prepare_data_for_db():
    # Get the last processed page from the database.
    last_processed_page = find_last_processed_page(db_path, table_name)

    # Open the PDF file.
    with fitz.open(pdf_path) as doc:
        # Start the loop from the next unprocessed page till the second last page.
        for i in range(last_processed_page + 1, len(doc) - 2):
            # Both start and end have a gap of 2.
            start_idx = i
            end_idx = i + 2

            # Get the text from the page.
            text = get_text_from_page(doc, start_idx, end_idx)
            logger.info(f"Text from page {start_idx} to {end_idx}:\n{text[:100]}")

            # Format the extracted text.
            formatted_text = punctuation_assistant(text)
            logger.info(f"Formatted text from page {start_idx} to {end_idx}")

            # Create a ThreadPoolExecutor
            with ThreadPoolExecutor() as executor:
                # Submit tasks to thread pool
                future_embeddings = executor.submit(get_embeddings, formatted_text)
                future_summary = executor.submit(summarize_textbook_pages_assistant, formatted_text)

                # Collect results as they become available
                embeddings_str = ','.join(map(str, future_embeddings.result()))
                logger.info(f"Embeddings of text from page {start_idx} to {end_idx}")

                summary_text = future_summary.result()
                logger.info(f"Summary of text from page {start_idx} to {end_idx}")

            # Embed the summary text.
            summary_embeddings_str = ','.join(map(str, get_embeddings(summary_text)))
            logger.info(f"Embeddings of summary of text from page {start_idx} to {end_idx}")

            # Column 2: GUID.
            guid = create_guid()
            logger.info(f"GUID created.")

            # Column 5: Target page
            target_page = start_idx + 1
            logger.info(f"Target page: {target_page}")

            # Column 6: Page range
            page_range = f"{start_idx},{target_page},{end_idx}"
            logger.info(f"Page range: {start_idx}, {target_page}, and {end_idx}.")

            # Column 8: Summary Embeddings


            # Prepare the data to be added to the database.
            response_data = {"guid": guid,
                             "author": author,
                             "title": book_title,
                             "target_page": target_page,
                             "page_range": page_range,
                             "summary": summary_text,
                             "summary_embeddings": summary_embeddings_str,
                             "text": formatted_text,
                             "embeddings": embeddings_str,
                             }

            # Append the data to the database.
            append_response_to_db(db_path, table_name, response_data)

            # Log the successful operation
            logger.info(f"Appended response to database.")
    return
