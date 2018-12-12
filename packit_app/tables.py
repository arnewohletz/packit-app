from .elements import User, DefaultClothingItem, Trip, TableElement, QueryItem
from .database import Database
from .sql_command_generator import SQLCommandGenerator as Cmd
from .table_helper import TableHelper
from .errors import *
import collections
from abc import ABC, abstractmethod


class TableFactory(ABC):
    """Abstract class that all table factory classes must implement"""
    column_types = collections.OrderedDict()

    @abstractmethod
    def create_table(self, element: TableElement):
        pass


class SingletonTableFactory(TableFactory):

    def create_table(self, element: TableElement):
        """Creates a Table object inside a :class:`Database` object.
        The table is not created if it already exists.

        :param element: defines the element type the table is supposed to
         store. The table then receives an appropriate name as well as the
         proper amount of columns with correct name and types.
        """
        self.column_types['id'] = 'INTEGER NOT NULL PRIMARY KEY ASC'
        table_layout_values = element.as_dict()

        for column in table_layout_values:
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

        else:
            #TODO: Add an 'IncompatibleTableElementError' raise
            pass


class UserSettingsTableFactory(TableFactory):

    def create_table(self, element: TableElement, user: User):
        self.column_types['id'] = 'INTEGER NOT NULL PRIMARY KEY ASC'
        table_layout_values = element.as_dict()

        for column in table_layout_values:
            if type(column) == str:
                self.column_types[column] = 'TEXT'
            elif type(column) == int:
                self.column_types[column] = 'INTEGER'
            elif type(column) == float:
                self.column_types[column] = 'REAL'


class Table:
    """

    """
    db = Database()
    helper = TableHelper()
    table_name = ""
    id = 1
    raised_errors = []

    def _element_already_exists(self, element: TableElement):
        """Checks whether the table already contains a entry with the same
        data"""

        self._execute_command(
            Cmd.get_return_element_command(self.table_name, element))

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
                self._execute_command(Cmd.get_add_element_to_table_command(
                    self.table_name,
                    self.id,
                    element))
                self.id += 1
                return True

        except ElementAlreadyExistsError as error:
            self.raised_errors.append(error)
            return False
            # TODO: Handle error with warning pop-up message

    def delete_element(self, element: TableElement):
        """
        Removes a single username entry from the table.
        :param :username, :gender
        :return: None
        """

        command = Cmd.get_remove_element_command(
            self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_matching_elements(self, *queries):
        """
        The function returns all matching elements from the table.

        Example:
        Table.get_elements(Male(), Name('Freddy')) returns all entries of the
        table that have the name value 'Freddy' and the gender attribute 'Male'

        :param queries:
        :return:
        """
        query_list = []

        for query in queries:
            query_list.append(query.as_dict())

        command = Cmd.get_return_matching_elements_command(
            self.table_name, query_list)

        result = [r for r in
                  self.helper.get_cursor_data_as_dictionary_generator(
                      self.db.cur.execute(command))]

        print("Hello: " + str(result))
        return result

    # TODO: Check if function is still required
    # def get_matching_elements_old(self, *query_items: QueryItem) -> list:
    #     """
    #     Returns the content of the table matching the passed :param:query_items.
    #
    #     :param: query_items is a list of :type:QueryItem objects.
    #     If no :param:query_item is passed, the complete table content is
    #     returned.
    #
    #     :param: query_items: dict
    #     :return: str
    #     """
    #
    #     command = Cmd.get_return_matching_elements_command(
    #         self.table_name, query_items=query_items)
    #
    #     result = [r for r in
    #               self.helper.get_cursor_data_as_dictionary_generator(
    #                   self.db.cur.execute(command))]
    #
    #     return result

    def clean_all_content(self):
        """
        Removes all data from the table.
        :return: None
        """
        command = Cmd.get_clean_all_content_command(
            self.table_name)
        self.db.cur.execute(command)
        self.id = 1

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors


class UserTable(Table):
    """
    UserTable manages the packit 'users' table within the Database which
    manages the registered users. It implements the TableStrategy interface.
    """

    table_name = 'users'

    def __init__(self, columns: collections.OrderedDict):
        command = Cmd.get_create_table_command(self.table_name,
                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def add_element(self, element: User):
        added = super(UserTable, self).add_element(element=element)
        return added


class GenderDefaultClothesTable(Table):
    table_name = 'gender_default_clothes'

    def __init__(self, columns: collections.OrderedDict):
        command = Cmd.get_create_table_command(self.table_name,
                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_default_clothes(self, gender):
        command = Cmd.get_return_element_command()


class TripTable(Table):
    table_name = 'trips'

    def __init__(self, columns: collections.OrderedDict):
        command = Cmd.get_create_table_command(self.table_name,
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

    # user_id: int, gender: str,

    def __init__(self, columns: collections.OrderedDict, user: User):
        self.table_name.format(str(user.user_id))
        command = Cmd.get_create_table_command(self.table_name,
                                               columns)
        self.db.cur.execute(command)
        self.db.connection.commit()

        self.add_default_clothes(gender)

    def add_default_clothes(self, gender: str) -> None:
        pass


class TripsTable(Table):
    table_name = "Trips"
    pass


class UserClothingSettingsTable(Table):
    table_name = "UserClothingSettings"
    pass


class UserTripClothing(Table):
    table_name = "UserTripClothingQuantity"
    pass


class GenderTable(Table):
    table_name = "Gender"
    pass


class ClothingItemsTable(Table):
    table_name = "ClothingItems"
    pass
