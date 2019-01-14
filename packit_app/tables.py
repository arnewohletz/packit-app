from .elements import User, DefaultClothingElement, Trip, TableDataElement, \
    TableField, Female, Male, Garment, Gender, UserTripGarmentAmount, \
    UserGarmentSettings
from .elements import *
# from .database import Database
from .sql_command_generator import SQLCommandGenerator as Cmd
from .table_helper import TableHelper
from .errors import *
import collections
from abc import ABC, abstractmethod
from overrides import overrides


class TableManager:
    gender_table = None
    user_table = None

    def __init__(self):
        table_factory = ConcreteTableFactory()
        self.gender_table = table_factory.create_table(Gender())
        self.user_table = table_factory.create_table(User())

    # def add_element(self, table, element):
    #     try:
    #         if not self._element_already_exists(element):
    #             self.db.execute_command(Cmd.get_add_element_to_table_command(
    #                 self.table_name,
    #                 self.id,
    #                 element))
    #             self.id += 1
    #             return True
    #
    #     except ElementAlreadyExistsError as error:
    #         self.raised_errors.append(error)
    #         return False


class TableFactory(ABC):
    """Abstract class that all table factory classes must implement"""

    # column_types = collections.OrderedDict()

    def __init__(self):
        self.column_types = collections.OrderedDict()

    @abstractmethod
    def create_table(self, element: TableDataElement):
        self.column_types = collections.OrderedDict()
        pass


class TableFactoryImpl(TableFactory):

    def __init__(self, database):
        super(TableFactoryImpl, self).__init__()
        self.database = database

        # for column in item.column_types:
        #     if type(item.column_types[column]) == str:
        #         self.column_types[column] = "TEXT"
        #     elif type(item.column_types[column]) == int:
        #         self.column_types[column] = "INTEGER"
        #     elif type(item.column_types[column]) == float:
        #         self.column_types[column] = "REAL"
        #
        # if isinstance(item, User):
        #     return UserTable(self.database, self.column_types)
        # elif isinstance(item, Gender):
        #     return Gender(self.database, self.column_types)

    def create_table(self, item: TableDataElement):
        """Creates a Table object inside a :class:`Database` object.
        The table is not created if it already exists.

        :param item: defines the element type the table is supposed to
         store. The table then receives an appropriate name as well as the
         proper amount of columns with correct name and types.
        """
        self.column_types.clear()

        for column in item.column_types:
            if type(item.column_types[column]) == str:
                self.column_types[column] = "TEXT"
            elif type(item.column_types[column]) == int:
                self.column_types[column] = "INTEGER"
            elif type(item.column_types[column]) == float:
                self.column_types[column] = "REAL"

        if isinstance(item, User):
            return UserTable(self.database, self.column_types)
        elif isinstance(item, Gender):
            return GenderTable(self.database, self.column_types)

        # table_layout_values = item.as_dict()
        # self.column_types.clear()
        #
        # # super(ConcreteTableFactory, self).__init__()
        # for column in table_layout_values:
        #     if type(column) == str:
        #         self.column_types[column] = 'TEXT'
        #     elif type(column) == int:
        #         self.column_types[column] = 'INTEGER'
        #     elif type(column) == float:
        #         self.column_types[column] = 'REAL'
        #
        # # table_layout_values.update({self.primary_key_column_name:"INTEGER NOT NULL PRIMARY KEY ASC"})
        # # table_layout_values.move_to_end(self.primary_key_column_name, last=False)
        #
        # if isinstance(element, User):
        #     return MyUserTable(self.database, self.column_types)
        # elif isinstance(element, Gender):
        #     return MyGenderTable(self.database, self.column_types)
        #
        # else:
        #     # TODO: Add an 'IncompatibleTableElementError' raise
        #     pass


# TODO: Delete this after TableFactoryImpl works
class ConcreteTableFactory(TableFactory):

    def create_table(self, element: TableDataElement):
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

        super(ConcreteTableFactory, self).__init__()
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


# class UserClothingSettingsTableFactory(TableFactory):
#
#     def create_table(self, element: TableElement, user: User):
#         self.column_types['id'] = 'INTEGER NOT NULL PRIMARY KEY ASC'
#         table_layout_values = element.as_dict()
#
#         for column in table_layout_values:
#             if type(column) == str:
#                 self.column_types[column] = 'TEXT'
#             elif type(column) == int:
#                 self.column_types[column] = 'INTEGER'
#             elif type(column) == float:
#                 self.column_types[column] = 'REAL'


class Table:
    """

    """
    # db = Database()
    db = None
    helper = TableHelper()
    table_name = ""
    primary_key_column_name = ""
    id = 1
    raised_errors = []

    def __init__(self, primary_key, column_types):
        column_types.update(
            {primary_key: "INTEGER NOT NULL PRIMARY KEY ASC"})
        column_types.move_to_end(primary_key, last=False)
        self.db.execute_command(Cmd.get_create_table_command(self.table_name,
                                                             column_types))

    def _element_already_exists(self, element: TableDataElement):
        """Checks whether the table already contains a entry with the same
        data"""

        self.db.execute_command(
            Cmd.get_return_element_command(self.table_name, element))

        data = self.db.cur.fetchall()
        if len(data) == 0:
            return False
        else:
            raise ElementAlreadyExistsError

    def add_element(self, element: TableDataElement):

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

    def delete_element(self, element: TableDataElement):
        """
        Removes a single username entry from the table.
        :param :username, :gender
        :return: None
        """

        command = Cmd.get_remove_element_command(
            self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def get_matching_elements(self, *field_values):
        """
        The function returns all matching elements from the table.

        Example:
        Table.get_matching_elements(Male(), Name('Freddy')) returns all entries
        of the table that have the name value 'Freddy' and the gender attribute
        'Male'

        :param queries:
        :return: list
        """

        all_queries_dict = {}
        for field_value in field_values:
            all_queries_dict.update(field_value)

        command = Cmd.get_return_matching_elements_command(
            self.table_name, all_queries_dict)

        # query_list = []
        # if queries:
        #     query_list = list(queries)
        #
        # # if queries:
        # #     for query in queries[0]:
        # #         query_list.append(query)
        # # query_list.append(query.as_dict())
        #
        # command = Cmd.get_return_matching_elements_command(
        #     self.table_name, query_list)

        result = [r for r in
                  self.helper.get_cursor_data_as_dictionary_generator(
                      self.db.cur.execute(command))]

        return result

    # def get_primary_key_value(self, *queries):
    #     result = self.get_matching_elements(queries)
    #     return result[0][self.primary_key_column_name]

    def get_primary_key_as_dict(self, element: TableDataElement):
        # element.column_types
        result = self.get_matching_elements(element.field)

        # for key in element.column_types:
        #     command += "'" + element.column_types[key] + "',"
        # result = self.get_matching_elements(*queries)

        # return result[0][self.primary_key_column_name]
        if len(result) > 0:
            return {self.primary_key_column_name: result[0][
                self.primary_key_column_name]}
        else:
            return

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors

    # def get_element_id(self, element) -> dict:
    #     """
    #     Returns element id as dictionary.
    #
    #     Requires a table element as argument. The returning dictionary contains
    #     either one or zero key value pairs in which case the element is not
    #     present in the table.
    #
    #     :param element: TableDataElement
    #     :return: dict(id_column_name, id_value)
    #     """


class MyGenderTable(Table):
    table_name = "Gender"
    primary_key_column_name = "GenderID"

    def __init__(self, database, columns):
        self.db = database
        super(MyGenderTable, self).__init__(self.primary_key_column_name,
                                            columns)


# class MyUserTable(Table):
#     table_name = 'User'
#     primary_key_column_name = "UserID"
#
#     def __init__(self, database, columns):
#         self.db = database
#         super(MyUserTable, self).__init__(self.primary_key_column_name,
#                                           columns)


class GarmentTable(Table):
    table_name = "Garment"
    primary_key_column_name = "GarmentID"

    def __init__(self, columns: collections.OrderedDict):
        super(GarmentTable, self).__init__(self.primary_key_column_name,
                                           columns)


class GenderTable(Table):
    table_name = "Gender"
    primary_key_column_name = "GenderID"

    def __init__(self, database, columns_types):
        self.db = database
        super(GenderTable, self).__init__(self.primary_key_column_name,
                                          columns_types)
        super(GenderTable, self).add_element(Gender(Male()))
        super(GenderTable, self).add_element(Gender(Female()))

    # table_name = "Gender"
    # primary_key_column_name = "GenderID"
    #
    # def __init__(self, columns: collections.OrderedDict):
    #     super(GenderTable, self).__init__(self.primary_key_column_name,
    #                                       columns)
    #     super(GenderTable, self).add_element(Gender(Male.value))
    #     super(GenderTable, self).add_element(Gender(Female.value))

    # super(GenderTable, self).add_element(Female().as_dict())
    # super(GenderTable, self).add_element(Male().as_dict())

    # @staticmethod
    # def get_primary_key_value(queries):
    #     result = Table.get_matching_elements(queries)
    #     return result[0][self.primary_key_column_name]

    # TODO:Check, if this override is still needed

    # def get_primary_key(self, queries):
    #     result = self.get_matching_elements(queries)
    #     return result[0][self.primary_key_column_name]


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

    def __init__(self, database, column_types):
        self.db = database
        super(UserTable, self).__init__(self.primary_key_column_name,
                                        column_types)

    # table_name = 'User'
    # primary_key_column_name = "UserID"
    #
    # def __init__(self, columns: collections.OrderedDict):
    #     super(UserTable, self).__init__(self.primary_key_column_name, columns)
    #
    # def _match_ids(self, element: User):
    #     print(element)
    #     content = element.as_dict()

    # Für die get_primary_key Methode wird eine List von QueryElements benötigt
    # da diese die get_matching_elements Methode aufruft
    # Da die _match_ids methode derzeit von der add_element Methode aufgerufen wird
    # liefert diese ein TableElement in diese Methode hinein
    # Ziel ist es daher, aus einem OrderedDict eine Liste von QueryElements zu machen

    # if content[GenderName.column_name] == "male":
    #
    #
    # for column in element.as_dict():
    #     if column == GenderName.column_name:
    #         # if content
    #         # content[column] = GenderTable.get_primary_key_value(column)
    #         # element.[column_name] = GenderTable.get_primary_key_value(
    #         #     value)
    #         query = {
    #             GenderName.column_name: content[GenderName.column_name]}
    #         result = GenderTable.get_primary_key_value(query)
    #
    # return result

    # @overrides
    # def add_element(self, element: User):
    #     # TODO: Transform [{name="Arne, gender="male"}] to [{name="Arne", gender=1}]
    #
    #     # gender_table = GenderTable.get_matching_elements()
    #
    #     # element.column_types[
    #     #     GenderName.column_name] = self.get_primary_key_value(
    #     #     element.as_dict())
    #     # element.column_types[
    #     #     GenderID.column_name] = self.get_primary_key_value(
    #     #     [{'gendername': 'male'}, {'username': "Arne"}])
    #     #
    #     # added = super(UserTable, self).add_element(element=element)
    #     # return added
    #
    #     # TODO: I have a User object at this point, containing a Gender object inside its column_types dictionary
    #     # How to get the GenderID from the Gender object?
    #
    #     GenderID = TableManager.gender_table.get_primary_key_value(
    #         element.column_types[GenderID.column_name])
    #     print("Done")
    #
    #     gender = element.column_types[GenderName.column_name]
    #
    #     # gender = element[0][GenderName.column_name]
    #
    #     # gender_id = Database.gender_table.get_matching_elements(
    #     #     dict(gender=gender))[0][GenderID.column_name]
    #     # element[0][gender] = gender_id
    #
    #     added = super(UserTable, self).add_element(element=element)
    #     return added

    # def get_primary_key_value(self, **kwargs):
    #     result = self.get_matching_elements(kwargs)
    #
    #     # for key in element.column_types:
    #     #     command += "'" + element.column_types[key] + "',"
    #     # result = self.get_matching_elements(*queries)
    #     return result[0][self.primary_key_column_name]


class UserTripGarmentAmountTable(Table):
    table_name = "UserTripGarmentAmount"
    primary_key_column_name = "UserTripGarmentAmountID"

    def __init__(self, columns: collections.OrderedDict):
        super(UserTripGarmentAmountTable, self).__init__(
            self.primary_key_column_name, columns)
