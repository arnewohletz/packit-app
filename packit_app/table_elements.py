from collections import OrderedDict
from abc import ABC
from .table_fields import *


class TableDataElement(ABC):
    column_types = None

    def __init__(self) -> None:
        self.column_types = OrderedDict()

    def get_as_dict(self) -> OrderedDict:
        return self.column_types

    # def get_id(self, *args, **kwargs) -> int:
    #     pass


class Gender(TableDataElement):

    def __init__(self, gender: GenderName = GenderName("male")) -> None:
        super(Gender, self).__init__()
        self.column_types[GenderName.column_name] = gender.field[
            GenderName.column_name]

    # def get_id(self, gender_name: str) -> int:


class Male(Gender):

    def __init__(self):
        super(Male, self).__init__(GenderName("male"))


class Female(Gender):

    def __init__(self):
        super(Female, self).__init__(GenderName("female"))


class User(TableDataElement):
    name = ""
    gender = None

    def __init__(self, username: Username = Username(""),
                 gender_id: GenderID = GenderID(1)) -> None:
        super(User, self).__init__()
        self.column_types[Username.column_name] = username.field[
            Username.column_name]
        self.column_types[GenderID.column_name] = gender_id.field[
            GenderID.column_name]


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
    def __init__(self, gender="", name="", is_default=False):
        super(Garment, self).__init__()
        self.column_types[GenderName.column_name] = gender
        self.column_types[GarmentName.column_name] = name
        self.column_types[GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableDataElement):
    pass


class UserGarmentSetting(TableDataElement):

    def __init__(self, user_id, garment_id):
        super(UserGarmentSetting, self).__init__()
        pass
