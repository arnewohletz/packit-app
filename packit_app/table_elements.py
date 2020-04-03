from abc import ABC
from collections import OrderedDict

from packit_app import table_fields as tf


class TableDataElement(ABC):

    def __init__(self) -> None:
        self.column_types: OrderedDict = OrderedDict()
        pass

    def get_as_dict(self) -> OrderedDict:
        return self.column_types


class Gender(TableDataElement):

    def __init__(self, gender: tf.GenderName = tf.GenderName("male")) -> None:
        super(Gender, self).__init__()
        self.column_types[tf.GenderName.column_name] = gender.field[
            tf.GenderName.column_name]


class Male(Gender):

    def __init__(self):
        super(Male, self).__init__(tf.GenderName("male"))


class Female(Gender):

    def __init__(self):
        super(Female, self).__init__(tf.GenderName("female"))


class User(TableDataElement):
    name = ""
    gender = None

    def __init__(self, username: tf.Username = tf.Username(""),
                 gender_id: tf.GenderID = tf.GenderID(1)) -> None:
        super(User, self).__init__()
        self.column_types[tf.Username.column_name] = username.field[
            tf.Username.column_name]
        self.column_types[tf.GenderID.column_name] = gender_id.field[
            tf.GenderID.column_name]


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
        self.column_types[tf.TripDestination.column_name] = destination
        self.column_types[tf.TripDateStart.column_name] = start_date
        self.column_types[tf.TripDateEnd.column_name] = end_date
        self.column_types[
            tf.TripTemperatureDayAverage.column_name] = day_average_temp
        self.column_types[tf.TripTemperatureDayMax.column_name] = day_max_temp
        self.column_types[tf.TripTemperatureDayMin.column_name] = day_min_temp
        self.column_types[
            tf.TripTemperatureNightIndoorAverage.column_name] = \
            night_average_indoor_temp
        self.column_types[tf.TripDaysWithSports.column_name] = sport_days
        self.column_types[tf.TripDaysWithoutSports.column_name] = no_sport_days
        self.column_types[tf.TripDaysInTransit.column_name] = transit_days


class Garment(TableDataElement):
    def __init__(self, gender_id: tf.GenderID = tf.GenderID(),
                 name: tf.GarmentName = tf.GarmentName(), is_default=False):
        super(Garment, self).__init__()
        self.column_types[tf.GenderID.column_name] = gender_id.get_value()
        self.column_types[tf.GarmentName.column_name] = name.get_value()
        self.column_types[tf.GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableDataElement):
    def __init__(self, user_id: tf.UserID = tf.UserID(),
                 trip_id: tf.TripID = tf.TripID(),
                 garment_id: tf.GarmentID = tf.GarmentID()):
        super(UserTripGarmentAmount, self).__init__()
        self.column_types[tf.UserID.column_name] = user_id.get_value()
        self.column_types[tf.TripID.column_name] = trip_id.get_value()
        self.column_types[tf.GarmentID.column_name] = garment_id.get_value()

        self.column_types[tf.TripGarmentTotalQuantity.column_name] = 0.0


class UserGarmentSetting(TableDataElement):

    def __init__(self, user_id: tf.UserID = tf.UserID(),
                 garment_id: tf.GarmentID = tf.GarmentID()):
        super(UserGarmentSetting, self).__init__()
        self.column_types[tf.UserID.column_name] = user_id.get_value()
        self.column_types[tf.GarmentID.column_name] = garment_id.get_value()

        self.column_types[tf.QuantityDayBelow0.column_name] = 0.0
        self.column_types[tf.QuantityDay0To10.column_name] = 0.0
        self.column_types[tf.QuantityDay10To20.column_name] = 0.0
        self.column_types[tf.QuantityDayAbove20.column_name] = 0.0
        self.column_types[tf.QuantityNightBelow20.column_name] = 0.0
        self.column_types[tf.QuantityNightAbove20.column_name] = 0.0
        self.column_types[tf.QuantityNoSportsDay.column_name] = 0.0
        self.column_types[tf.QuantitySportsDay.column_name] = 0.0
        self.column_types[tf.QuantityTransitDay.column_name] = 0.0
