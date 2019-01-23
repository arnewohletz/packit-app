from collections import OrderedDict
import abc
from .table_fields import *


class TableDataElement(abc.ABC):
    fields = None

    def __init__(self) -> None:
        self.fields = OrderedDict()

    def get_as_dict(self) -> OrderedDict:
        return self.fields


class Gender(TableDataElement):

    def __init__(self, gender: GenderName = GenderName("male")) -> None:
        super(Gender, self).__init__()
        self.fields[GenderName.column_name] = gender.field[
            GenderName.column_name]


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
        self.fields[Username.column_name] = username.field[
            Username.column_name]
        self.fields[GenderID.column_name] = gender_id.field[
            GenderID.column_name]


# TODO: Update column_types
class DefaultClothingElement(TableDataElement):
    def __init__(self, gender="", clothing_item=""):
        super(DefaultClothingElement, self).__init__()
        self.fields['gender'] = gender
        self.fields['clothing_item'] = clothing_item


class Trip(TableDataElement):
    def __init__(self, destination, start_date, end_date, day_average_temp,
                 day_max_temp, day_min_temp, night_average_indoor_temp,
                 sport_days, no_sport_days, transit_days):
        super(Trip, self).__init__()
        self.fields[TripDestination.column_name] = destination
        self.fields[TripDateStart.column_name] = start_date
        self.fields[TripDateEnd.column_name] = end_date
        self.fields[
            TripTemperatureDayAverage.column_name] = day_average_temp
        self.fields[TripTemperatureDayMax.column_name] = day_max_temp
        self.fields[TripTemperatureDayMin.column_name] = day_min_temp
        self.fields[
            TripTemperatureNightIndoorAverage.column_name] = night_average_indoor_temp
        self.fields[TripDaysWithSports.column_name] = sport_days
        self.fields[TripDaysWithoutSports.column_name] = no_sport_days
        self.fields[TripDaysInTransit.column_name] = transit_days


class Garment(TableDataElement):
    def __init__(self, gender, name, is_default):
        super(Garment, self).__init__()
        self.fields[GenderName.column_name] = gender
        self.fields[GarmentName.column_name] = name
        self.fields[GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableDataElement):
    pass


class UserGarmentSettings(TableDataElement):
    pass
