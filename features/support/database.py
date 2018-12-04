from packit_app import database, tables
from packit_app.sql_command_generator import SQLCommandGenerator


class DatabaseHelper:

    def __init__(self):
        self.db = database.Database()
        self.conn = self.db.connection
        self.cur = self.db.cur

    def print_table(self, table_name):
        self.db.cur.execute(
            """SELECT * FROM {0}""".format(table_name)
        )
        content = tuple(self.db.cur.fetchall())
        for row in content:
            print(list(row))

        if content == ():
            print('<user table empty>')



#
# class UserTableHelper:
#
#     def __init__(self):
#         self.db = database.Database()
#         self.user_table = tables.UserTable()
#         self.generator = SQLCommandGenerator()
#
#     def drop_user_table(self):
#         command = self.generator.get_drop_table_command(
#             self.user_table.table_name)
#         self.db.connection.execute(command)
#         self.db.connection.commit()
