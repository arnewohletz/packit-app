from packit_app.table_elements import User
from packit_app.tables import UserTable
from packit_app.table_helper import TableHelper
from packit_app.sql_command_generator import SQLCommandGenerator


class UserTableHelper:

    def get_user_id(self, user_table: UserTable, user: User) -> int:
        user_id = 0
        helper = TableHelper()
        generator = SQLCommandGenerator()
        command = generator.get_return_element_command(table_name=user_table, element=User)
        helper.get_row_content_as_dictionary()

        return user_id
