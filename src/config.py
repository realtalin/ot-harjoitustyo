import os

from dotenv import load_dotenv

this_directory = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(this_directory, '..', '.env'))

DATABASE_NAME = os.getenv('DATABASE_NAME') or 'database.sqlite'
