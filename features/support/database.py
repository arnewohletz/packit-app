from packit_app import database
import logging


class DatabaseHelper:

    def __init__(self) -> None:
        self.db = database.Database()
        self.conn = self.db.connection
        self.cur = self.db.cur

    # def print_table(self, table_name: str) -> None:
    #     self.db.cur.execute(
    #         """SELECT * FROM {0}""".format(table_name)
    #     )
    #     content = tuple(self.db.cur.fetchall())
    #     for row in content:
    #         print(list(row))
    #
    #     if content == ():
    #         print('<table has no content>')

    def log_table(self, table_name: str) -> None:
        self.db.cur.execute(
            """SELECT * FROM {0}""".format(table_name)
        )
        content = tuple(self.db.cur.fetchall())

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.warning("Table content:")
        for row in content:
            logger.warning(list(row))

        if content == ():
            logging.error("-table has no content-")
