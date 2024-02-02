import sqlite3


def df_to_sqlite3(df, db_path, table_name):
    """
    Writes a pandas DataFrame to a SQLite3 database, inserting each row into the database one by one.

    Parameters:
    - df: The pandas DataFrame to insert into the SQLite database.
    - db_path: String representing the path to the SQLite database file.
    - table_name: The name of the table into which the DataFrame should be inserted.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table if it doesn't exist
    cols = ', '.join(f'"{col}" TEXT' for col in df.columns)
    cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({cols})')

    # Insert DataFrame rows one by one
    for index, row in df.iterrows():
        values = ', '.join(f'"{val}"' for val in row.values)
        cur.execute(f'INSERT INTO {table_name} VALUES ({values})')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()