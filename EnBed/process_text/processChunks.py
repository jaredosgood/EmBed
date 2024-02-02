from datetime import datetime
from EnBed.process_text.punctuation_assistant import punctuation_assistant
from EnBed.logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger('my_application')


def get_current_timestamp():
    return datetime.now().isoformat(timespec='seconds')

def process_chunks(chunks_dict):
    chunks_list = []
    for _, chunk_text in chunks_dict.items():
        try:
            logger.info(f"{get_current_timestamp()}: Calling 'punctuation_assistant' function with chunk_text...")
            processed_text = punctuation_assistant(str(chunk_text))
        except Exception as e:
            logger.error(f"{get_current_timestamp()}: Exception occurred while calling 'punctuation_assistant': {e}")
            print(f"An error occurred while processing the chunks. Check log_file.log for more information.")
            return

        chunks_list.append(processed_text)
    try:
        processed_chunks = ''.join(chunks_list)
        logger.info(f"{get_current_timestamp()}: 'process_chunks' function ended successfully.")
        print("Chunks were successfully processed.")
    except Exception as e:
        logger.error(f"{get_current_timestamp()}: Exception occurred while joining processed chunks: {e}")
        print(f"An error occurred while joining the processed chunks. Check log_file.log for more information.")
        return

    return processed_chunks