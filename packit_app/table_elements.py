from collections import OrderedDict
from abc import ABC
from .table_fields import *


class TableDataElement(ABC):
    i = 0
    column_types = None

    def __init__(self) -> None:
        self.column_types = OrderedDict()
        self.id = 0

    def as_dict(self) -> OrderedDict:
        return self.column_types

    # def get_id_as_dict(self):
    #
    #     pass


# class Female(GenderName):
#     value = "female"
#     GenderID = 2
#
#
# class Male(GenderName):
#     value = "male"
#     GenderID = 1

class Gender(TableDataElement):
    # default_table = Database.gender_table

    # def __init__(self, gender: GenderName = GenderName("male"),
    #              gender_id: GenderID = GenderID(1)) -> None:
    def __init__(self, gender: GenderName = GenderName("male")) -> None:
        # def __init__(self, gender: TableField = Male()) -> None:
        super(Gender, self).__init__()
        # self.column_types[GenderID.column_name] = gender_id.field[
        #     GenderID.column_name]
        self.column_types[GenderName.column_name] = gender.field[
            GenderName.column_name]

        # self.id_column_name = "GenderID"
        # # self.column_types[GenderName.column_name] = gender.value
        # self.column_types["name"] = gender.value
        # self.column_types[self.id_column_name] = gender.id
        # self.GenderID = None

    # @classmethod
    # def get_id(cls):
    #     result = Gender.default_table.get_matching_elements(cls)
    #     return result


class Male(Gender):
    column_name = "Name"

    def __init__(self):
        super(Male, self).__init__(GenderName("male"))
        # super(Male, self).__init__(GenderName("male"), GenderID(1))
        # self.column_types[GenderName.column_name] = "male"
        # self.column_types[GenderID.column_name] = 1
        # self.field[GenderID.column_name] = 1
        # self.field[GenderName.column_name] = "male"
    # def __init__(self):
    #     super(Male, self).__init__()
    #     self.GenderID = 1
    #     self.value = "male"


class Female(Gender):
    column_name = "Name"

    def __init__(self):
        # super(Female, self).__init__(GenderName("female"), GenderID(2))
        super(Female, self).__init__(GenderName("female"))
        # self.column_types[GenderName.column_name] = "female"
        # self.column_types[GenderID.column_name] = 2
        # self.field[GenderID.column_name] = 2
        # self.field[GenderName.column_name] = "female"
        # self.GenderID = 2
        # self.value = "female"


# class Female(Gender):
#     # value = "female"
#     # GenderID = 2
#
#     def __init__(self):
#         super(Female, self).__init__()
#         self.GenderID = 2
#         self.value = "female"
#
#
# class Male(Gender):
#     # value = "male"
#     # GenderID = 1
#
#     def __init__(self):
#         super(Male, self).__init__()
#         self.GenderID = 1
#         self.value = "male"


class User(TableDataElement):
    name = ""
    gender = None

    # default_table = Database.user_table

    # gender_table = GenderTable(collections.OrderedDict())

    def __init__(self, username: Username = Username(""),
                 gender_id: GenderID = GenderID(1)) -> None:
        super(User, self).__init__()
        self.column_types[Username.column_name] = username.field[
            Username.column_name]
        self.column_types[GenderID.column_name] = gender_id.field[
            GenderID.column_name]

    # def __init__(self, username=Username(""), gender=Male()):
    #     super(User, self).__init__()
    #     self.username = username
    #     self.gender = gender
    #     self.column_types[self.username.column_name] = self.username.value
    #     self.column_types[self.gender.id_column_name] = self.gender.GenderID
    #     # self.column_types[GenderID.column_name] = gender.GenderID
    #     self.column_types[GenderID.column_name] = gender.GenderID
    # self.column_types[
    #     GenderName.column_name] = self.gender_table.get_primary_key_value(
    #     gender)

    # def get_primary_key_value(self):
    #     db.execute(Cmd.return_matching_elements_command(self.default_table, self.name, self.gender))

    # def get_id(self):
    #     result = self.default_table.get_matching_elements(self, self.column_types)
    #     return result


# TODO: Update column_types
class DefaultClothingElement(TableDataElement):
    def __init__(self, gender="", clothing_item=""):
        super(DefaultClothingElement, self).__init__()
        self.column_types['gender'] = gender
        self.column_types['clothing_item'] = clothing_item


class Trip(TableDataElement):
    def __init__(self, destination, start_date, end_date, day_average_temp,
                 day_max_temp, day_min_temp, night_average_indoor_temp,
                 sport_days, no_sport_days, transit_days):
        super(Trip, self).__init__()
        self.column_types[TripDestination.column_name] = destination
        self.column_types[TripDateStart.column_name] = start_date
        self.column_types[TripDateEnd.column_name] = end_date
        self.column_types[
            TripTemperatureDayAverage.column_name] = day_average_temp
        self.column_types[TripTemperatureDayMax.column_name] = day_max_temp
        self.column_types[TripTemperatureDayMin.column_name] = day_min_temp
        self.column_types[
            TripTemperatureNightIndoorAverage.column_name] = night_average_indoor_temp
        self.column_types[TripDaysWithSports.column_name] = sport_days
        self.column_types[TripDaysWithoutSports.column_name] = no_sport_days
        self.column_types[TripDaysInTransit.column_name] = transit_days


class Garment(TableDataElement):
    def __init__(self, gender, name, is_default):
        super(Garment, self).__init__()
        self.column_types[GenderName.column_name] = gender
        self.column_types[GarmentName.column_name] = name
        self.column_types[GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableDataElement):
    pass


class UserGarmentSettings(TableDataElement):
    pass
