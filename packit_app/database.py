import sqlite3
from packit_app import constants
from packit_app.tables import TableFactoryImpl
from typing import Optional


class Database:
    """
    The Database class manages the initial creation of the SQLite database file
    and contains the connection and cursor variables needed to interact with
    the database. Since the Database class is a singleton, its sole
    instantiation is referred to by calling the get_instance() method.
    """
    connection: Optional[sqlite3.Connection] = None
    cur: Optional[sqlite3.Cursor] = None
    errors: list = []
    db_location = constants.DB_LOCATION

    def __init__(self) -> None:
        self.connection = sqlite3.connect(self.db_location)
        self.cur = self.connection.cursor()
        self.table_factory = TableFactoryImpl(self)
        assert isinstance(self.cur, sqlite3.Cursor)

    def execute_command(self, command: str) -> None:
        """Executes any given SQL query on the connected database"""
        assert self.cur and self.connection is not None
        self.cur.execute(command)
        self.connection.commit()

    def close_connection(self) -> None:
        """Closes the database connection (unlocks it)."""
        assert self.connection is not None
        self.connection.close()
