import time
from EnBed.logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger('EnBed.process_text.punctuation_assistant')

RETRY_WAIT_TIME = 300  # 5 minutes
MAX_RETRIES = 3  # maximum number of retries

def retry_on_rate_limit_error(func, *args, **kwargs):
    """
    A wrapper function that retries the given function after waiting for RETRY_WAIT_TIME seconds
    if an Exception is encountered.
    """
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            retry_count += 1
            time.sleep(RETRY_WAIT_TIME)

    logging.error(f"The function {func.__name__} has reached the maximum retry limit")
    return None
