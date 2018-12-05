from .elements import TableElement, QueryElement
import collections


class SQLCommandGenerator:

    @staticmethod
    def get_add_element_to_table_command(table_name: str, value_id: int,
                                         element: TableElement):

        command = "INSERT INTO " + table_name + ' VALUES(' + str(
            value_id) + ","

        for key in element.column_types:
            command += "'" + element.column_types[key] + "',"

        command = command[:-1] + ")"
        print(command)

        return command

    @staticmethod
    def get_create_table_command(table_name: str,
                                 columns: collections.OrderedDict):
        command = "CREATE TABLE IF NOT EXISTS " + table_name + "("

        for name, kind in columns.items():
            command += name + " " + kind + ", "

        command = command[:-2] + ")"

        return command

    @staticmethod
    def get_clean_all_content_command(table_name: str):
        command = "DELETE FROM " + table_name
        return command

    @staticmethod
    def get_drop_table_command(table_name: str):
        command = "DROP TABLE IF EXISTS " + table_name
        return command

    @staticmethod
    def get_remove_element_command(table_name: str, element: TableElement):

        command = "DELETE FROM " + table_name + " WHERE ("

        for key in element.column_types:
            command += key + " = '" + element.column_types[key] + "' AND "

        command = command[:-5] + ")"

        return command

    @staticmethod
    def get_return_element_from_table_command(table_name,
                                              element: TableElement):
        columns = list(element.column_types.keys())

        command = "SELECT * FROM " + table_name + " WHERE "
        for data in columns:
            command += data + " = '" + element.column_types[data] + "' AND "

        command = command[:-5]

        return command

    @staticmethod
    def get_return_all_elements_from_table_command(table_name):

        command = "SELECT * FROM " + table_name

        return command

    @staticmethod
    def get_return_all_matching_elements_from_table_command(table_name, element: QueryElement):
        element.queries
