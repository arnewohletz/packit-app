from .table_elements import TableElementIdentifier
import collections


class SQLCommandGenerator:

    @staticmethod
    def _concatenate_fields_with_and(fields: dict) -> str:
        result = ""
        for key, value in fields.items():
            result += str(key) + "="
            if type(value) == str:
                result += "'" + str(value) + "' AND "
            else:
                result += str(value) + " AND "

        return result[:-5]

    @staticmethod
    def get_update_element_data_command(table_name: str,
                                        identifier: TableElementIdentifier,
                                        data: dict) -> str:
        """
        Returns an SQL command to update one or multiple data values for a
        single table element

        :param table_name: Table name as String
        :param identifier: identifies table element to update column values in
        :param data: `dict` which contains column names and the new values that
        are supposed to be updated
        :rtype: str
        """
        command = "UPDATE " + table_name + " SET "

        command += SQLCommandGenerator._concatenate_fields_with_and(data)
        command += " WHERE "
        command += SQLCommandGenerator._concatenate_fields_with_and(
            identifier.get_fields_as_dict())

        return command

    @staticmethod
    def get_add_element_to_table_command(table_name: str,
                                         primary_key_column_name: str,
                                         element_id: int,
                                         data: dict) -> str:

        command = "INSERT INTO " + table_name + " (" + \
                  primary_key_column_name + " ,"

        column_data = value_data = ""

        for key, value in data.items():
            column_data += key + ", "
            if type(value) == str:
                value_data += "'" + str(value) + "', "
            else:
                value_data += str(value) + ", "

        column_data = column_data[:-2]
        value_data = value_data[:-2]

        command += column_data + ") VALUES (" + str(
            element_id) + ", " + value_data + ")"

        return command

    # @staticmethod
    # def OLD_get_add_element_to_table_command(table_name: str, element_id: int,
    #                                          element: TableElementIdentifier) -> str:
    #
    #     # TODO: Change SQL command into this:
    #     # insert into Gender(Name, GenderID) values('male', 1);
    #     # now:
    #     # insert into Gender(1, 'male')
    #     # this is not good because it relies on the proper order of the
    #     # OrderedDict, the TableDataElement brings. But I want to be able to
    #     # add new data, that contains more than the TableDataElement data
    #     # e.g. GarmentTable will hold the Garment object data, which is
    #     # 'name' and 'gender_id' but the information, whether this garment's
    #     # quantities must be specified by all new users must also be in it, but
    #     # it is not part of the Garment object. A new GarmentTable entry is
    #     # supposed to look like this then:
    #     # garment_table.add_element(Garment(Name('pants'), GenderID(gender_id)),
    #     #   QuantityMustBeSpecified(True))
    #     # so it requires a Garment object and a QuantityMustBeSpecified object
    #
    #     command = "INSERT INTO " + table_name + ' VALUES(' + str(
    #         element_id) + ","
    #
    #     for key in element.fields:
    #         command += "'" + str(element.fields[key]) + "',"
    #
    #     command = command[:-1] + ")"
    #
    #     return command

    @staticmethod
    def get_clean_all_content_command(table_name: str) -> str:
        command = "DELETE FROM " + table_name
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
    def get_remove_element_command(table_name: str,
                                   element: TableElementIdentifier) -> str:

        command = "DELETE FROM " + table_name + " WHERE "

        command += SQLCommandGenerator._concatenate_fields_with_and(
            element.get_fields_as_dict())

        return command

    @staticmethod
    def get_return_matching_elements_command(table_name: str,
                                             query_items: dict = None):
        """
        Returns a proper SQL command for selecting matching items of the given
        :param:table_name that are defined by :param:query_items.
        :param: query_items must be of type list where the list items itself
        are dictionaries, containing the column and value of a :param:QueryItem.

        Example:

        get_return_matching_elements_command(table_name="foo", [{foo:bar}, {bar:foo}]

        :param table_name: str
        :param query_items: list of dictionaries
        :return:
        """

        command = "SELECT * FROM " + table_name
        counter = {}

        if query_items:
            for column, value in query_items.items():
                if column not in counter:
                    counter[column] = 1
                else:
                    counter[column] += 1
        else:
            return command

        command = command + " WHERE ("

        for column, value in query_items.items():
            if counter[column] > 1:
                command += column + " = '" + str(value) + "' OR "
                counter[column] -= 1
            elif counter[column] == 1:
                command += column + " = '" + str(value) + "' AND "

        command = command[:-5] + ")"

        return command
