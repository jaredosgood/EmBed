import sqlite3
import pandas as pd
import logging
from EnBed.logging_config import setup_logging


setup_logging()
logger = logging.getLogger('EnBed.db_functions.close_connection')

def append_response_to_db(db_path, table_name, response_data):
    """
    Appends a single response row to a SQLite database.

    Parameters:
    - response_data: Dictionary containing response data.
    - db_path: String representing the path to the SQLite database file.
    - table_name: The name of the table where the data is appended.
    """
    # Convert response data to DataFrame
    response_df = pd.DataFrame([response_data])
    logger.info(f"Response data: {response_df.head(1)}")

    # Connect to the SQLite database
    with sqlite3.connect(db_path) as conn:
        response_df.to_sql(table_name, con=conn, if_exists='append', index=False)
        logger.info(f"Appended response data to {table_name} table in {db_path}")
