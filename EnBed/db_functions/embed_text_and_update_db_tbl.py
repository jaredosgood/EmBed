import logging

from openai import OpenAI

from EnBed.db_functions.close_connection import close_connection
from EnBed.db_functions.create_connection import create_connection
from EnBed.logging_config import setup_logging


# Set up logging
setup_logging()
logger = logging.getLogger('EnBed.process_text.embed_text_and_update_db_tbl')


def embed_text_and_update_db_tbl(db_path: str, table_name: str, column: str, write_to_column: str, id_column: str):
    conn, cursor = create_connection(db_path)                           # Connect to the given SQLite database
    cursor.execute(f"SELECT {id_column}, {column} FROM {table_name};")  # Select data
    rows = cursor.fetchall()                                            # Fetch all rows
    client = OpenAI()                                                   # Create an OpenAI client

    for row in rows:
        result = row[1]                             # Define results as the data from the '{column}' column
        response = client.embeddings.create(        # Create an embedding from the data
            input=result,
            model="text-embedding-3-large"
        )
        embedding = response.data[0].embedding          # Define the embedding as the response data
        embedding_str = ','.join(map(str, embedding))   # Convert the embedding to a CSV string

        # Update the 'embeddings' column with the new embedding
        cursor.execute(f"UPDATE {table_name} SET {write_to_column} = ? WHERE {id_column} = ?", (embedding_str, row[0]))
        logger.info(f"Updated {table_name} with {write_to_column} for {id_column} {row[0]}")
    conn.commit()
    close_connection(conn, cursor)
    logger.info(f"Connection to {db_path} closed")
    return


# embed_text_and_update_db_tbl("/Users/jdo/EnBed/EnBed/db/EnBed.sqlite",
#                              "algorithms_table",
#                              "summary",
#                              "summary_embeddings",
#                              "id")
