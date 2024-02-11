import sqlite3
from openai import OpenAI

from EnBed.db_functions.close_connection import close_connection
from EnBed.db_functions.create_connection import create_connection


def embed_text_and_update_db_tbl(db_path: str, table_name: str, text_column: str, id_column: str):
    # Connect to your SQLite database
    conn = create_connection(db_path)
    c = conn.cursor()

    # Select the data from the table
    c.execute(f"SELECT {id_column}, {text_column} FROM {table_name};")
    rows = c.fetchall()

    client = OpenAI()

    for row in rows:
        result = row[1]  # Get the data to send for embedding
        response = client.embeddings.create(
            input=result,
            model="text-embedding-3-large"
        )
        embedding = response.data[0].embedding

        # Update the 'embeddings' column with the new embedding
        c.execute(f"UPDATE {table_name} SET embeddings = ? WHERE {id_column} = ?", (embedding, row[0]))

    # Commit the changes and close the connection
    conn.commit()
    close_connection(conn, c)