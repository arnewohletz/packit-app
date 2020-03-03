from abc import ABC
from collections import OrderedDict

from packit_app.table_fields import GarmentID, GarmentIsDefault, GarmentName, \
    GenderID, GenderName, TripDateEnd, TripDateStart, TripDaysInTransit, \
    TripDaysWithSports, TripDaysWithoutSports, TripDestination, \
    TripTemperatureDayAverage, TripTemperatureDayMax, TripTemperatureDayMin, \
    TripTemperatureNightIndoorAverage, UserID, Username


class TableDataElement(ABC):

    def __init__(self) -> None:
        self.column_types: OrderedDict = OrderedDict()
        pass

    def get_as_dict(self) -> OrderedDict:
        return self.column_types


class Gender(TableDataElement):

    def __init__(self, gender: GenderName = GenderName("male")) -> None:
        super(Gender, self).__init__()
        self.column_types[GenderName.column_name] = gender.field[
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
            TripTemperatureNightIndoorAverage.column_name] = \
            night_average_indoor_temp
        self.column_types[TripDaysWithSports.column_name] = sport_days
        self.column_types[TripDaysWithoutSports.column_name] = no_sport_days
        self.column_types[TripDaysInTransit.column_name] = transit_days


class Garment(TableDataElement):
    def __init__(self, gender_id: GenderID = GenderID(),
                 name: GarmentName = GarmentName(), is_default=False):
        super(Garment, self).__init__()
        self.column_types[GenderID.column_name] = gender_id.get_value()
        self.column_types[GarmentName.column_name] = name.get_value()
        self.column_types[GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableDataElement):
    pass


class UserGarmentSetting(TableDataElement):

    def __init__(self, user_id: UserID = UserID(),
                 garment_id: GarmentID = GarmentID()):
        super(UserGarmentSetting, self).__init__()
        self.column_types[UserID.column_name] = user_id.get_value()
        self.column_types[GarmentID.column_name] = garment_id.get_value()
