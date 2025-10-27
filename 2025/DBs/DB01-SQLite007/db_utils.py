# db_utils.py
import sqlite3
import os
from dotenv import load_dotenv

# All paths are inside the .env file
load_dotenv()
AUTH_DB = os.getenv('AUTH_DB')
DATA_DB = os.getenv('DATA_DB')
AUTH_SQL = os.getenv('AUTH_SQL')
DATA_SQL = os.getenv('DATA_SQL')


def initiate_db_with_data(file_name: str, db_name: str) -> None:
    """Initialize a SQLite database with SQL commands from a file."""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"SQL file {file_name} not found")
    with sqlite3.connect(db_name) as conn:
        conn.executescript(open(file_name, 'r').read())
        conn.commit()

def init_db() -> None:
    """Initialize both CTF databases if they don't exist."""
    if not os.path.exists(AUTH_DB) or not os.path.exists(DATA_DB):
        initiate_db_with_data(AUTH_SQL, AUTH_DB)
        initiate_db_with_data(DATA_SQL, DATA_DB)
