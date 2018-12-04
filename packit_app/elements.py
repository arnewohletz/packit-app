import collections
from abc import ABC


class Element(ABC):
    def __init__(self):
        pass


class QueryElement(ABC, Element):
    """Query object to use for database searches"""
    queries = []

    def __init__(self, *args, **kwargs):
        for arg in args:
            if type(arg) is Gender:
                self.queries.append(dict({'gender':arg.gender}))

    def get_query(self):
        """Returns element queries as list of tuples"""
        # for query in self.queries:
        #     column = query.keys()
        # query = []
        # for item in l:
        #     self.queries.append(dict({'gender': 'male'}))
        #     queries.append("".join(x for x in item.keys()))
        return self.queries


class Gender(QueryElement):
    def __init__(self):
        if type(gender) == Female or type(gender) == Male:
            self.queries['gender'] = gender.gender
        if gender.lower() == "male" or gender.lower() == "female":
            self.queries['gender'] = gender
        else:
            raise ValueError("Gender must be either 'male' or 'female")


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
        self.column_types['name'] = name
        self.column_types['gender'] = gender


class DefaultClothingItem(TableElement):
    def __init__(self, gender="", clothing_item=""):
        self.column_types['gender'] = gender
        self.column_types['clothing_item'] = clothing_item


class Trip(TableElement):
    def __init__(self, destination="", start_date="", end_date=""):
        self.column_types['destination'] = destination
        self.column_types['start_date'] = start_date
        self.column_types['end_date'] = end_date
