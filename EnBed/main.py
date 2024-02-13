import logging
import os
import sqlite3
from EnBed.db_functions.prepare_data_for_db import prepare_data_for_db
from EnBed.logging_config import setup_logging
from EnBed.utilities.retry_on_rate_limit_errors import retry_on_rate_limit_error
from EnBed.db_functions.create_table_static import create_table_if_not_exists
from EnBed.utilities.constants import DB_PATH, TABLE_NAME

setup_logging()
logger = logging.getLogger('EnBed.main')
API_KEY = os.environ.get("OPENAI_API_KEY")


def main():
    db_connection = sqlite3.connect(DB_PATH)
    my_table_name = TABLE_NAME
    create_table_if_not_exists(db_connection, my_table_name)
    retry_on_rate_limit_error(prepare_data_for_db)
    return


if __name__ == '__main__':
    main()
