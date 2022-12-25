import os
import sqlite3

from config import DATABASE_NAME

this_directory = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(this_directory, DATABASE_NAME))
connection.row_factory = sqlite3.Row


def get_connection():
    return connection
