import collections
from abc import ABC
# from packit_app.tables import Table


class Element(ABC):
    def __init__(self):
        pass


class QueryItem(Element):
    """Query object to use for database searches"""
    column_name = ""
    value = ""

    @classmethod
    def get_query(cls):
        """Returns element queries as list of tuples"""
        return dict({cls.column_name: cls.value})


class Name(QueryItem):
    column_name = 'name'

    @classmethod
    def get_query(cls, name):
        cls.value = name
        return super(Name, cls).get_query()


class Gender(QueryItem):
    column_name = "gender"


class Female(Gender):
    value = "female"


class Male(Gender):
    value = "male"


class TableElement(Element):
    column_types = collections.OrderedDict()

    def get_default_values(self) -> collections.OrderedDict:
        """Returns default table column names and value type as OrderedDict"""
        return self.column_types


class User(TableElement):
    def __init__(self, name="", gender=""):
        self.column_types[Name.column_name] = name
        self.column_types[Gender.column_name] = gender
        # self.column_types['name'] = name
        # self.column_types['gender'] = gender


class DefaultClothingItem(TableElement):
    def __init__(self, gender="", clothing_item=""):
        self.column_types['gender'] = gender
        self.column_types['clothing_item'] = clothing_item


class Trip(TableElement):
    def __init__(self, destination="", start_date="", end_date=""):
        self.column_types['destination'] = destination
        self.column_types['start_date'] = start_date
        self.column_types['end_date'] = end_date
