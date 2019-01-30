from collections import OrderedDict
import abc
from .table_fields import *


class TableElementIdentifier(abc.ABC):
    fields = None

    def __init__(self) -> None:
        self.fields = OrderedDict()

    def get_fields_as_dict(self) -> dict:
        return dict(self.fields)


class Gender(TableElementIdentifier):

    def __init__(self, gender: GenderName = GenderName("male")) -> None:
        super(Gender, self).__init__()
        self.fields[GenderName.column_name] = gender.data[
            GenderName.column_name]


class Male(Gender):

    def __init__(self):
        super(Male, self).__init__(GenderName("male"))


class Female(Gender):

    def __init__(self):
        super(Female, self).__init__(GenderName("female"))


class User(TableElementIdentifier):
    name = ""
    gender = None

    def __init__(self, username: Username = Username(""),
                 gender_id: GenderID = GenderID(1)) -> None:
        super(User, self).__init__()
        self.fields[Username.column_name] = username.data[
            Username.column_name]
        self.fields[GenderID.column_name] = gender_id.data[
            GenderID.column_name]


# class DefaultClothingElement(TableDataElement):
#     def __init__(self, gender="", clothing_item=""):
#         super(DefaultClothingElement, self).__init__()
#         self.fields['gender'] = gender
#         self.fields['clothing_item'] = clothing_item


class Trip(TableElementIdentifier):
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


class Garment(TableElementIdentifier):
    def __init__(self, gender_id: GenderID = GenderID(1),
                 name: GarmentName = GarmentName(""),
                 is_default: GarmentIsDefault = GarmentIsDefault(True)):
        super(Garment, self).__init__()
        self.fields[GenderID.column_name] = gender_id.data[
            GenderID.column_name]
        self.fields[GarmentName.column_name] = name.data[
            GarmentName.column_name]
        # self.fields[GarmentIsDefault.column_name] = is_default.field[
        #     GarmentIsDefault.column_name]


class UserTripGarmentAmount(TableElementIdentifier):
    pass


class UserGarmentSettings(TableElementIdentifier):
    pass
