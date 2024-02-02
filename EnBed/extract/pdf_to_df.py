from EnBed.db_functions.db_ops import find_last_processed_page, create_or_update_entry
from EnBed.process_text.punctuation_assistant import punctuation_assistant
from EnBed.utilities.create_guid import create_guid
import fitz
from EnBed.logging_config import setup_logging
import logging


AUTHOR = "Lil' Bobby"
BOOK_TITLE = "The Big Book of Gangster Nation"

setup_logging()
logger = logging.getLogger('EnBed.export.pdf_to_df')

def get_text_from_page(doc, start_idx, end_idx):
    text_from_page = ""
    for i in range(start_idx, min(end_idx, len(doc))):
        page = doc.load_page(i)
        text_from_page += page.get_text().encode("utf8").decode("utf8") + "\f"
    return text_from_page


def pdf_to_df(pdf_path, db_path, table_name):
    entries = []
    last_processed_page = find_last_processed_page(db_path, table_name)

    with fitz.open(pdf_path) as doc:
        for i in range(last_processed_page + 1, len(doc) - 2):
            start_idx = i
            end_idx = i + 3
            text = get_text_from_page(doc, start_idx, end_idx)
            formatted_text = punctuation_assistant(text)
            target_page = start_idx + 1
            page_range = f"{start_idx},{target_page},{end_idx - 1}"
            create_or_update_entry(db_path, table_name, target_page, page_range, formatted_text)
            print(f"Processed page: {target_page}")
            guid = create_guid()
            entries.append({"guid": guid,
                            "author": AUTHOR,
                            "book_title": BOOK_TITLE,
                            "target_page": target_page,
                            "page_range": page_range,
                            "text": formatted_text,
                        })

    #     df = pd.DataFrame(entries)
    #     df.columns = ["target_page", "page_range", "text"]
    # return df

# Example usage
pdf_path = "/Users/jdo/Library/CloudStorage/OneDrive-Personal/ASU Courses/SER 222/M6/ser222_02_02_hw02.pdf"
# df = pdf_to_df(pdf_path)
# print(df.head())