import collections
from abc import ABC


class Element(ABC):
    def __init__(self):
        pass


class QueryItem(Element):
    column_name = ""
    value = ""

    def as_dict(self):
        return dict({self.column_name: self.value})


class TableElement(Element):
    column_types = collections.OrderedDict()

    def as_dict(self):
        return self.column_types


class Gender(QueryItem):
    column_name = "gender"

    def __init__(self, gender):
        super(Gender, self).__init__()
        self.value = gender.value


class Female(Gender):
    value = "female"


class Male(Gender):
    value = "male"


class Name(QueryItem):
    column_name = "name"

    def __init__(self, value):
        super(Name, self).__init__()
        self.value = value


class User(TableElement):
    def __init__(self, name="", gender=""):
        super(User, self).__init__()
        self.column_types[Name.column_name] = name
        self.column_types[Gender.column_name] = gender


# class DefaultClothingItem(TableElement):
#     def __init__(self, gender="", clothing_item=""):
#         self.column_types['gender'] = gender
#         self.column_types['clothing_item'] = clothing_item


# class Trip(TableElement):
#     def __init__(self, destination="", start_date="", end_date=""):
#         self.column_types['destination'] = destination
#         self.column_types['start_date'] = start_date
#         self.column_types['end_date'] = end_date
