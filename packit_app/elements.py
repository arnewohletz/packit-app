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


class Female(Gender):
    value = "female"


class Male(Gender):
    value = "male"


class Name(QueryItem):
    column_name = "name"

    def __init__(self, value):
        super(Name, self).__init__()
        self.value = value


class Destination(QueryItem):
    column_name = "destination"

    def __init__(self, value):
        super(Destination, self).__init__()



class User(TableElement):
    def __init__(self, name="", gender=Gender()):
        super(User, self).__init__()
        self.column_types[Name.column_name] = name
        self.column_types[Gender.column_name] = gender.value


# TODO: Update column_types
class DefaultClothingItem(TableElement):
    def __init__(self, gender="", clothing_item=""):
        super(DefaultClothingItem, self).__init__()
        self.column_types['gender'] = gender
        self.column_types['clothing_item'] = clothing_item


# TODO: Update column_types
class Trip(TableElement):
    def __init__(self, destination="", start_date="", end_date=""):
        super(Trip, self).__init__()
        self.column_types['destination'] = destination
        self.column_types['start_date'] = start_date
        self.column_types['end_date'] = end_date


class Trip(TableElement):
    def __init____(self, destination, start_date, end_date, day_average_temp,
                   day_max_temp, day_min_temp, night_average_indoor_temp,
                   sport_days, no_sport_days, transit_days):
        super(Trip, self).__init__()
        self.column_types[]


class UserClothingSetting(TableElement):
    def __init__(self, ):
