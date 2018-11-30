import sqlite3
from packit_app import constants


class Database:
    """
    The Database class manages the initial creation of the SQLite database file
    and contains the connection and cursor variables needed to interact with
    the database. Since the Database class is a singleton, its sole
    instantiation is refered to by calling the get_instance() method.
    """
    connection = None
    cur = None
    errors = []
    db_location = constants.DB_LOCATION

    def __init__(self):
        self.connection = sqlite3.connect(self.db_location)
        self.cur = self.connection.cursor()

    def close_connection(self):
        """Closes the database connection (unlocks it)."""
        self.connection.close()

    # @staticmethod
    # def get_instance():
    #     """ Static access method. Returns the sole Database object"""
    #     if Database.__instance is None:
    #         Database()
    #         Database.connection = sqlite3.connect(Database.DB_LOCATION)
    #         Database.cur = Database.connection.cursor()
    #     return Database.__instance
    #
    # def __init__(self):
    #     """ Virtually private constructor. """
    #     if Database.__instance is not None:
    #         raise Exception("This class is a singleton!")
    #     else:
    #         Database.__instance = self
    #
    # def close_connection(self):
    #     """Closes the database connection (unlocks it)."""
    #     self.connection.close()
