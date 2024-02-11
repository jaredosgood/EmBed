import sqlite3
import logging
from EnBed.logging_config import setup_logging


setup_logging()
logger = logging.getLogger('EnBed.db_functions.close_connection')

def close_connection(conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    """
    Close the database connection
    :param conn: connection object
    :param cursor: cursor object
    """
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
        logger.info("SQLite connection is closed.")
