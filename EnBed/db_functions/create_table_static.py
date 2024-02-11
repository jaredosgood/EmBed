import sqlite3
import logging
from EnBed.logging_config import setup_logging


setup_logging()
logger = logging.getLogger('EnBed.db_functions.create_table_static')
def create_table_if_not_exists(db_connection, table_name):
    cursor = db_connection.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        guid CHAR(128) NOT NULL,
        author CHAR(128),
        title CHAR(128),
        target_page INT,
        page_range CHAR(128),
        summary TEXT,
        summary_embeddings BLOB,
        text TEXT,
        embeddings BLOB
    )
    """)
    db_connection.commit()
    cursor.close()

# # Example usage:
# db_connection = sqlite3.connect('mydatabase.db')
# my_table_name = "new_book_table"
# create_table_if_not_exists(db_connection, my_table_name)
