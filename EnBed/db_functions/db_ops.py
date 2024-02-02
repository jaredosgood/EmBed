import sqlite3
from typing import Any, Tuple



def find_last_processed_page(db_path: str, table_name: str) -> int:
    # Forming the SQL query to fetch the maximum value from the `target_page` column.
    # This indicates the last processed page in the given table.
    query = f'SELECT MAX(target_page) FROM {table_name}'

    # Executing the above SQL query with the provided `db_path`.
    # The `execute_sql_query` function is expected to return a result set (a list),
    # where the first element is the highest page number processed.
    result = execute_sql_query(db_path, query)

    # Returning the result from the query if it exists and is not None.
    # If the result does not exist or is None (-1 is returned),
    # it indicates no pages have been processed yet.
    return result[0] - 1 if result and result[0] is not None else -1


def execute_sql_query(db_path: str, query: str) -> Tuple[Any]:
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
    return result
