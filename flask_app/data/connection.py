
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



# ----------------------------------------------------
import sqlite3

def get_db_connection():
    conn = sqlite3.connect("test.db")
    conn.row_factory = sqlite3.Row  # Returns results as dictionaries
    return conn


