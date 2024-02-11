import sqlite3
from typing import Tuple
import logging
from EnBed.logging_config import setup_logging


setup_logging()
logger = logging.getLogger('EnBed.db_functions.close_connection')

def create_connection(db_file: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Create a database connection to a SQLite database specified by the db_file
    :param db_file: database file
    :return: connection object and cursor object
    """
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        logger.info(f"Connected to SQLite database: {db_file}")
        return conn, cursor
    except sqlite3.Error as e:
        logger.error(f"Error connecting to SQLite database: {e}")
        return None, None


# # Usage example
# if __name__ == "__main__":
#     # Specify your SQLite database file name
#     db_file = "example.db"
#
#     # Create a connection and cursor
#     conn, cursor = create_connection(db_file)
#
#     # Perform any database operations using conn and cursor here
#
#     # Close the connection and cursor
#     close_connection(conn, cursor)
