from .elements import User, TableElement, Trip, \
    DefaultClothingItem, QueryItem
from .database import Database
from .sql_command_generator import SQLCommandGenerator
from .table_helper import TableHelper
from .errors import *
import collections
from abc import ABC, abstractmethod


class TableFactory(ABC):
    """Abstract class that all table factory classes must implement"""
    column_types = collections.OrderedDict()

    @abstractmethod
    def create_table(self, element: TableElement):
        """Creates a table inside the :class:`Database` database

        The passed parameter :param:`element` defines the column names and
        types
        :param element: :class:`TableElement` object that are supposed to be
        managed by the table
        """
        pass


class Table:
    db = Database()
    helper = TableHelper()
    table_name = ""
    id = 1
    raised_errors = []

    def _element_already_exists(self, element: TableElement):
        """Checks whether the table already contains a entry with the same
        data"""

        command = SQLCommandGenerator.get_return_element_from_table_command(
            self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

        data = self.db.cur.fetchall()
        if len(data) == 0:
            return False
        else:
            raise ElementAlreadyExistsError

    def _execute_command(self, command):
        self.db.cur.execute(command)
        self.db.connection.commit()

    def add_element(self, element: TableElement):

        try:
            if not self._element_already_exists(element):
                command = SQLCommandGenerator.get_add_element_to_table_command(
                    self.table_name,
                    self.id,
                    element)
                self.db.cur.execute(command)
                self.db.connection.commit()
                self.id += 1

        # TODO: Don't like the error handling. How else to make sure Behave notices them?
        except ElementAlreadyExistsError as error:
            print("Error: The user already exists")
            self.raised_errors.append(error)
            pass

    def delete_element(self, element: TableElement):
        """
        Removes a single username entry from the table.
        :param :username, :gender
        :return: None
        """

        command = SQLCommandGenerator.get_remove_element_command(
            self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_single_element(self, element: TableElement):

        command = SQLCommandGenerator.get_return_element_from_table_command(
            self.table_name, element)

        result = self.helper.get_row_content_as_dictionary(
            self.db.cur.execute(command))

        return result

    def get_elements(self, *query_items: QueryItem) -> dict:
        """
        Returns the content of the table matching the passed :param:query_items.

        :param: query_items is a list of :type:QueryItem objects.
        If no :param:query_item is passed, the complete table content is
        returned.

        :param query_items:
        :return: str
        """

        command = SQLCommandGenerator.get_return_matching_elements_command(
            self.table_name, conditions=query_items)

        result = self.helper.get_query_data_as_list_of_dictionaries(
            self.db.cur.execute(command))

        return result

    def get_all_elements(self) -> list:
        """
        Returns the complete content of the table as a list of dictionaries,
        each dictionary representing one row of data.
        :return: list
        """

        command = SQLCommandGenerator.get_return_matching_elements_command(
            self.table_name)
        result = [r for r in
                  self.helper.get_query_data_as_list_of_dictionaries(
                      self.db.cur.execute(command))]
        return result

    def clean_all_content(self):
        """
        Removes all data from the table.
        :return: None
        """
        command = SQLCommandGenerator.get_clean_all_content_command(
            self.table_name)
        self.db.cur.execute(command)
        self.id = 1

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors


class ConcreteTableFactory(TableFactory):

    def create_table(self, element: TableElement) -> Table:
        self.column_types['id'] = 'INTEGER NOT NULL PRIMARY KEY ASC'
        column_default_values = element.get_default_values()

        for column in column_default_values:
            if type(column) == str:
                self.column_types[column] = 'TEXT'
            elif type(column) == int:
                self.column_types[column] = 'INTEGER'
            elif type(column) == float:
                self.column_types[column] = 'REAL'

        if isinstance(element, User):
            return UserTable(self.column_types)
        elif isinstance(element, Trip):
            return TripTable(self.column_types)
        elif isinstance(element, DefaultClothingItem):
            return UserSettingsTable(self.column_types)
        else:
            pass


class UserTable(Table):
    """
    UserTable manages the packit 'users' table within the Database which
    manages the registered users. It implements the TableStrategy interface.
    """

    table_name = 'users'

    def __init__(self, columns: collections.OrderedDict):
        command = SQLCommandGenerator.get_create_table_command(self.table_name,
                                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def add_element(self, element: User):
        super(UserTable, self).add_element(element=element)


class GenderDefaultClothesTable(Table):
    table_name = 'gender_default_clothes'

    def __init__(self, columns: collections.OrderedDict):
        command = SQLCommandGenerator.get_create_table_command(self.table_name,
                                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_default_clothes(self, gender):
        command = SQLCommandGenerator.get_return_element_from_table_command()


class TripTable(Table):
    table_name = 'trips'

    def __init__(self, columns: collections.OrderedDict):
        command = SQLCommandGenerator.get_create_table_command(self.table_name,
                                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()


class UserSettingsTable(Table):
    """
    UserSettingsTable contains the individual settings of each user. It
    implements the TableStrategy interface.
    """
    table_name = 'user_{0}_default_clothes'
    default_clothes = None

    def __init__(self, user_id: int, gender: str,
                 columns: collections.OrderedDict):
        self.table_name.format(str(user_id))
        command = SQLCommandGenerator.get_create_table_command(self.table_name,
                                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

        self.add_default_clothes(gender)

    def add_default_clothes(self, gender: str) -> None:
        pass

    def get_default_clothes(self, gender: Gender) -> list:
        pass
