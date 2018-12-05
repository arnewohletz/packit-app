import collections
from abc import ABC
from packit_app.tables import Table


class Element(ABC):
    def __init__(self):
        pass


class QueryElement(ABC, Element):
    """Query object to use for database searches"""
    queries = []
    element = None

    def __init__(self, table_element: Element, *args, **kwargs):
        # self.element = table_element
        # self.element.column_types
        for arg in args:
            if type(arg) is Gender:
                self.queries.append(dict({Gender.column_name: arg.gender}))

    def get_query(self):
        """Returns element queries as list of tuples"""
        # for query in self.queries:
        #     column = query.keys()
        # query = []
        # for item in l:
        #     self.queries.append(dict({'gender': 'male'}))
        #     queries.append("".join(x for x in item.keys()))
        return self.queries


class Name(QueryElement):
    column_name = 'name'


class Gender(ABC, QueryElement):
    gender = ""
    column_name = "gender"

    # def __init__(self):
    #     if type(gender) == Female or type(gender) == Male:
    #         self.queries['gender'] = gender.gender
    #     if gender.lower() == "male" or gender.lower() == "female":
    #         self.queries['gender'] = gender
    #     else:
    #         raise ValueError("Gender must be either 'male' or 'female")


class Female(Gender):
    def __init__(self):
        self.gender = "female"


class Male(Gender):
    def __init__(self):
        self.gender = "male"


class TableElement(ABC, Element):
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
