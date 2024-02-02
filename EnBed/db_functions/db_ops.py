import sqlite3


def create_or_update_entry(db_path, table_name, target_page, page_range, text):
    """
    Creates or updates a database entry for a given page.

    Parameters:
    - db_path: Path to the SQLite database file.
    - table_name: Name of the table to insert/update data.
    - target_page: The page currently being processed.
    - page_range: The range of pages processed for this entry.
    - text: The processed text to save.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table if it does not exist
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            target_page INTEGER UNIQUE,
            page_range TEXT,
            text TEXT
        )
    ''')

    # Update or insert the data
    cur.execute(f'''
        INSERT INTO {table_name} (target_page, page_range, text)
        VALUES (?, ?, ?)
        ON CONFLICT(target_page) DO UPDATE SET
            page_range = excluded.page_range,
            text = excluded.text
    ''', (target_page, page_range, text))

    # Commit and close
    conn.commit()
    conn.close()

def find_last_processed_page(db_path, table_name):
    """
    Finds the last processed page number from the database.

    Parameters:
    - db_path: Path to the SQLite database file.
    - table_name: Name of the table.

    Returns:
    - The last page number processed or -1 if none have been processed.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(f'SELECT MAX(target_page) FROM {table_name}')
    result = cur.fetchone()
    conn.close()

    if result and result[0] is not None:
        return result[0]
    else:
        return -1