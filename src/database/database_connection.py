import os
import sqlite3

this_directory = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(this_directory, "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_connection():
    return connection
