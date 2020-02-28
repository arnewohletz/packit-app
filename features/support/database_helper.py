from packit_app import database


class DatabaseHelper:

    def __init__(self) -> None:
        self.db = database.Database()
        self.conn = self.db.connection
        self.cur = self.db.cur

    def print_table(self, table_name: str) -> None:

        if self.db.cur is not None:
            self.db.cur.execute(
                """SELECT * FROM {0}""".format(table_name)
            )
            content = tuple(self.db.cur.fetchall())
            for row in content:
                print(list(row))

            if content == ():
                print('<user table empty>')
