import logging
import os
from EnBed.db_functions.prepare_data_for_db import prepare_data_for_db
from EnBed.logging_config import setup_logging
from EnBed.utilities.retry_on_rate_limit_errors import retry_on_rate_limit_error

setup_logging()
logger = logging.getLogger('EnBed.main')
API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    retry_on_rate_limit_error(prepare_data_for_db)
    return


if __name__ == '__main__':
    main()
