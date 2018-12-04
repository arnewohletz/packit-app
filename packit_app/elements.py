import collections
from abc import ABC


class TableElement(ABC):
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
