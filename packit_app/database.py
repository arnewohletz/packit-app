import sqlite3
from packit_app import constants
from .tables import TableFactoryImpl


class Database:
    """
    The Database class manages the initial creation of the SQLite database file
    and contains the connection and cursor variables needed to interact with
    the database. Since the Database class is a singleton, its sole
    instantiation is referred to by calling the get_instance() method.
    """
    connection = None
    cur = None
    errors = []
    db_location = constants.DB_LOCATION

    def __init__(self):
        self.connection = sqlite3.connect(self.db_location)
        self.cur = self.connection.cursor()
        self.table_factory = TableFactoryImpl(self)

    def execute_command(self, command):
        """Executes any given SQL query on the connected database"""
        self.cur.execute(command)
        self.connection.commit()

    def close_connection(self):
        """Closes the database connection (unlocks it)."""
        self.connection.close()
