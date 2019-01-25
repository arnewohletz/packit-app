from .table_elements import *
from .table_fields import TableField
from .sql_command_generator import SQLCommandGenerator as Cmd
from .table_helper import TableHelper
from .errors import *
import collections
from abc import ABC, abstractmethod


class Table:
    """
    Parent class for all tables inside the database.

    .. warning::
        Please do not create tables by instantiating this class, but use the
        `TableFactoryImpl.create_table()` method for this purpose.

    Each table requires a `primary_key` column, which saves an integer value
    for each `TableDataElement` that is added to the table.

    :param primary_key: string name that the primary key column is supposed to
        have.
    :param column_types: dictionary that holds a key-value pair for each column
        , where the key holds the column name and the value contains the type
        information.
    """
    db = None
    helper = TableHelper()
    table_name = ""
    primary_key_column_name = ""
    id = 1
    raised_errors = []

    def __init__(self, database, primary_key_column_name: str,
                 column_types) -> None:
        self.db = database
        column_types.update(
            {primary_key_column_name: "INTEGER NOT NULL PRIMARY KEY ASC"})
        column_types.move_to_end(primary_key_column_name, last=False)
        self.db.execute_command(Cmd.get_create_table_command(self.table_name,
                                                             column_types))

    def _element_already_exists(self, element: TableDataElement):
        """Checks whether the table already contains a entry with the same
        data"""

        self.db.execute_command(Cmd.get_return_matching_elements_command(
            self.table_name, element.get_fields_as_dict()))

        data = self.db.cur.fetchall()
        if len(data) == 0:
            return False
        else:
            raise ElementAlreadyExistsError

    def add_element(self, element: TableDataElement,
                    *data: TableField) -> bool:
        """
        Adds a single `TableDataElement` to the table.

        :param element: element to be added
        :return: None
        """

        added_data = element.get_fields_as_dict()
        for field in data:
            added_data.update(field.get_field_as_dict())

        try:
            if not self._element_already_exists(element):
                self.db.execute_command(Cmd.get_add_data_to_table_command(
                    self.table_name,
                    self.primary_key_column_name,
                    self.id,
                    added_data))
                self.id += 1
                return True

        except ElementAlreadyExistsError as error:
            self.raised_errors.append(error)
            return False
            # TODO: Handle error with warning pop-up message

    def clean_all_content(self):
        """
        Removes all data from the table. Column types are not removed.

        :return: None
        """
        command = Cmd.get_clean_all_content_command(
            self.table_name)
        self.db.cur.execute(command)
        self.id = 1

    def delete_element(self, element: TableDataElement):
        """
        Removes a single data `TableDataElement` from the table.

        :param element: `TableDataElement` that is supposed to be removed from
            the table.
        :return: None
        """

        command = Cmd.get_remove_element_command(
            self.table_name, element)
        self.db.cur.execute(command)
        self.db.connection.commit()

    def _get_matching_elements(self, fields: dict):

        command = Cmd.get_return_matching_elements_command(
            self.table_name, fields)

        result = [r for r in
                  self.helper.get_cursor_data_as_dictionary_generator(
                      self.db.cur.execute(command))]

        return result

    def get_element(self, element: TableDataElement) -> list:
        """
        Returns full table data of an `TableDataElement` within a dictionary.
        If the element cannot be found, an empty list is returned.

        Example:
        ``Table.get_element(User(Username('Harry'), Male())) returns the data
        of a male user named Harry.

        :param element: Should be a valid `TableDataElement` type for the
            `Table` type it is applied on.
        :rtype: list, containing either one or zero dictionaries, depending on
            whether the element has been found or not.
        """
        queries = dict(element.fields)

        return self._get_matching_elements(queries)

    def get_matching_elements(self, *field_values: TableField) -> list:
        """
        Returns all matching table elements as a list dictionaries.

        `TableField`
        Zero, one or more dictionaries of type :class:`~packit_app.field_values.TableField`
        can to be passed as ``field_values``. If none are passed, all table
        elements are returned. Any passed ``field_value`` functions as a
        filter, where only elements fulfilling all filter conditions are
        returned.

        Example:
        ``Table.get_matching_elements(Username('Freddy')), Male()`` returns all
        entries of the table that have the username 'Freddy' and is of gender
        `Male`.

        :param field_values: Zero, one or more `TableField` objects
        :rtype: list of dictionaries, if one or more elements are found. Each
            dictionary contains the complete data of each found
            `TableDataElement`. An empty list is returned in case no match is
            found.
        """

        queries = {}
        for field_value in field_values:
            queries.update(field_value.field)

        return self._get_matching_elements(queries)

    def get_errors(self) -> list:
        """
        Returns a list of all errors that have been raised inside the table
        :return:
        """
        return self.raised_errors

    # TODO: Empty function of table specific content
    def get_primary_key_as_dict(self, element: TableDataElement):
        result = self.get_element(element)

        if len(result) > 0:
            return result[0][self.primary_key_column_name]
        else:
            return


class GarmentTable(Table):
    table_name = "Garment"
    primary_key_column_name = "GarmentID"

    def __init__(self, database, column_types: collections.OrderedDict):
        super(GarmentTable, self).__init__(database,
                                           self.primary_key_column_name,
                                           column_types)


class GenderTable(Table):
    table_name = "Gender"
    primary_key_column_name = "GenderID"

    def __init__(self, database, column_types):
        super(GenderTable, self).__init__(database,
                                          self.primary_key_column_name,
                                          column_types)
        super(GenderTable, self).add_element(Male())
        super(GenderTable, self).add_element(Female())


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


class UserTable(Table):
    """
    UserTable manages the packit 'users' table within the Database which
    manages the registered users. It implements the TableStrategy interface.
    """

    table_name = 'User'
    primary_key_column_name = "UserID"

    def __init__(self, database, column_types):
        super(UserTable, self).__init__(database, self.primary_key_column_name,
                                        column_types)

    # def add_element(self, element: TableDataElement, *data_fields: TableField):
    #     combined_data_fields = {}
    #
    #     combined_data_fields.update(element.get_fields_as_dict())
    #
    #     if len(data_fields) > 0:
    #         for data_field in data_fields:
    #             combined_data_fields.update(data_field.get_field_as_dict())


class UserTripGarmentAmountTable(Table):
    table_name = "UserTripGarmentAmount"
    primary_key_column_name = "UserTripGarmentAmountID"

    def __init__(self, columns: collections.OrderedDict):
        super(UserTripGarmentAmountTable, self).__init__(
            self.primary_key_column_name, columns)


class TableFactory(ABC):
    """Abstract class that all table factory classes must implement"""

    def __init__(self):
        self.column_types = collections.OrderedDict()

    @abstractmethod
    def create_table(self, element: TableDataElement):
        pass


class TableFactoryImpl(TableFactory):
    """The sole purpose of this class is to create `Table` objects."""

    def __init__(self, database):
        super(TableFactoryImpl, self).__init__()
        self.database = database

    def create_table(self, element: TableDataElement) -> Table:
        """Creates a Table object inside a :class:`Database` object.

        Item must be an implementation of the `TableDataElement` interface,
        which defines the resulting type of the table, that is returned.
        The proper column types are assigned to the table, depending on the
        default input value of each `TableField`, that `item` contains.
        The column names are derived accordingly.

        :param element: defines the element type the table is supposed to
         store. Must be of type `TableDataElement`.
        :rtype: `Table`
        """
        self.column_types.clear()

        for column in element.fields:
            if type(element.fields[column]) == str:
                self.column_types[column] = "TEXT"
            elif type(element.fields[column]) == int:
                self.column_types[column] = "INTEGER"
            elif type(element.fields[column]) == float:
                self.column_types[column] = "REAL"

        if isinstance(element, User):
            return UserTable(self.database, self.column_types)
        elif isinstance(element, Gender):
            return GenderTable(self.database, self.column_types)
        elif isinstance(element, Garment):
            return GarmentTable(self.database, self.column_types)
