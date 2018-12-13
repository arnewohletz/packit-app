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


class ConcreteTableFactory(TableFactory):

    def create_table(self, element: TableElement):
        """Creates a Table object inside a :class:`Database` object.
        The table is not created if it already exists.

        :param element: defines the element type the table is supposed to
         store. The table then receives an appropriate name as well as the
         proper amount of columns with correct name and types.
        """
        primary_key_column_name = ""

        # def __init__(self, columns: collections.OrderedDict):
        #     columns.update(
        #         {
        #             self.primary_key_column_name: "INTEGER NOT NULL PRIMARY KEY ASC"})
        #     columns.move_to_end(self.primary_key_column_name, last=False)
        table_layout_values = element.as_dict()
        #
        # table_layout_values[primary_key] = "INTEGER NOT NULL PRIMARY KEY ASC"

        for column in table_layout_values:
            if type(column) == str:
                self.column_types[column] = 'TEXT'
            elif type(column) == int:
                self.column_types[column] = 'INTEGER'
            elif type(column) == float:
                self.column_types[column] = 'REAL'

        # table_layout_values.update({self.primary_key_column_name:"INTEGER NOT NULL PRIMARY KEY ASC"})
        # table_layout_values.move_to_end(self.primary_key_column_name, last=False)

        if isinstance(element, User):
            return UserTable(self.column_types)
        elif isinstance(element, Trip):
            return TripTable(self.column_types)
        elif isinstance(element, Garment):
            return GarmentTable(self.column_types)
        elif isinstance(element, Gender):
            return GenderTable(self.column_types)
        elif isinstance(element, UserTripGarmentAmount):
            return UserTripGarmentAmountTable(self.column_types)
        elif isinstance(element, UserGarmentSettings):
            return UserGarmentSettingsTable(self.column_types)

        else:
            # TODO: Add an 'IncompatibleTableElementError' raise
            pass


class UserClothingSettingsTableFactory(TableFactory):

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
    primary_key_column_name = ""
    id = 1
    raised_errors = []

    def __init__(self, primary_key, data_columns):
        data_columns.update(
            {primary_key: "INTEGER NOT NULL PRIMARY KEY ASC"})
        data_columns.move_to_end(primary_key, last=False)
        self.db.execute_command(Cmd.get_create_table_command(self.table_name,
                                                             data_columns))

    def _element_already_exists(self, element: TableElement):
        """Checks whether the table already contains a entry with the same
        data"""

        self.db.execute_command(
            Cmd.get_return_element_command(self.table_name, element))

        data = self.db.cur.fetchall()
        if len(data) == 0:
            return False
        else:
            raise ElementAlreadyExistsError

    def add_element(self, element: TableElement):

        try:
            if not self._element_already_exists(element):
                self.db.execute_command(Cmd.get_add_element_to_table_command(
                    self.table_name,
                    self.id,
                    element))
                self.id += 1
                return True

        except ElementAlreadyExistsError as error:
            self.raised_errors.append(error)
            return False
            # TODO: Handle error with warning pop-up message

    def clean_all_content(self):
        """
        Removes all data from the table.
        :return: None
        """
        command = Cmd.get_clean_all_content_command(
            self.table_name)
        self.db.cur.execute(command)
        self.id = 1

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

    def get_primary_key_value(self, *queries):
        result = self.get_matching_elements(queries)
        return result[0][self.primary_key_column_name]

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors


class GarmentTable(Table):
    table_name = "Garment"
    primary_key_column_name = "GarmentID"

    def __init__(self, columns: collections.OrderedDict):
        super(GarmentTable, self).__init__(self.primary_key_column_name,
                                           columns)


class GenderTable(Table):
    table_name = "Gender"
    primary_key_column_name = "GenderID"

    def __init__(self, columns: collections.OrderedDict):
        super(GenderTable, self).__init__(self.primary_key_column_name,
                                          columns)


class TripTable(Table):
    table_name = "Trip"
    primary_key_column_name = "TripID"

    def __init__(self, columns: collections.OrderedDict):
        super(TripTable, self).__init__(self.primary_key_column_name, columns)


class UserGarmentSettingsTable(Table):
    """
    UserSettingsTable contains the individual settings of each user. It
    implements the TableStrategy interface.
    """
    table_name = "UserGarmentSettings"
    primary_key_column_name = "UserGarmentSettingsID"

    def __init__(self, columns: collections.OrderedDict):
        super(UserGarmentSettingsTable, self).__init__(
            self.primary_key_column_name, columns)

    # def __init__(self, columns: collections.OrderedDict, user: User):
    #     self.table_name.format(str(user.user_id))
    #     command = Cmd.get_create_table_command(self.table_name,
    #                                            columns)
    #     self.db.cur.execute(command)
    #     self.db.connection.commit()
    #
    #     self.add_default_clothes(gender)
    #
    # def add_default_clothes(self, gender: str) -> None:
    #     pass


class UserTable(Table):
    """
    UserTable manages the packit 'users' table within the Database which
    manages the registered users. It implements the TableStrategy interface.
    """

    table_name = 'User'
    primary_key_column_name = "UserID"

    def __init__(self, columns: collections.OrderedDict):
        super(UserTable, self).__init__(self.primary_key_column_name, columns)

    def add_element(self, element: User):
        added = super(UserTable, self).add_element(element=element)
        return added


class UserTripGarmentAmountTable(Table):
    table_name = "UserTripGarmentAmount"
    primary_key_column_name = "UserTripGarmentAmountID"

    def __init__(self, columns: collections.OrderedDict):
        super(UserTripGarmentAmountTable, self).__init__(
            self.primary_key_column_name, columns)
