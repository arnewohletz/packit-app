import collections
from abc import ABC
# from .database import Database


class Element(ABC):
    def __init__(self):
        pass


class QueryItem(Element):
    """
    A QueryItem represents a single column of a TableItem.

    Each QueryItem type holds the the column name it is saved in.
    """
    def __init__(self):
        super(QueryItem, self).__init__()
        self.column_name = ""
        self.value = ""

    # id = 0

    def as_dict(self):
        """
        Returns the column name and value as a dictionary
        :return: dict
        """
        return dict({self.column_name: self.value})


class TableElement(Element):
    # id = 0
    # column_types = collections.OrderedDict()
    # default_table = None

    def __init__(self):
        self.column_types = collections.OrderedDict()
        self.id = 0

    def as_dict(self):
        return self.column_types

    def get_id(self):
        pass



class GarmentName(QueryItem):
    value = "name"


class GarmentIsDefault(QueryItem):
    value = "isDefault"


class GenderID(QueryItem):
    column_name = "genderID"


class GenderName(QueryItem):
    column_name = "gender"


class Female(GenderName):
    value = "female"
    genderID = 2


class Male(GenderName):
    value = "male"
    genderID = 1


class Username(QueryItem):
    column_name = "username"

    def __init__(self, value):
        super(Username, self).__init__()
        self.value = value


class TripTemperatureDayAverage(QueryItem):
    column_name = "day_average_temp"


class TripTemperatureDayMax(QueryItem):
    column_name = "dayMaxTemp"


class TripTemperatureDayMin(QueryItem):
    column_name = "dayMinTemp"


class TripDestination(QueryItem):
    column_name = "destination"

    def __init__(self, value):
        super(TripDestination, self).__init__()


class TripTemperatureNightIndoorAverage(QueryItem):
    column_name = "night_average_indoor_temp"


class TripDaysInTransit(QueryItem):
    column_name = "days_in_transit"


class TripDaysWithSports(QueryItem):
    column_name = "days_without_sports"


class TripDaysWithoutSports(QueryItem):
    column_name = "days_with sports"


class TripDateEnd(QueryItem):
    column_name = "end_date"


class TripDateStart(QueryItem):
    column_name = "start_date"


class User(TableElement):
    name = ""
    gender = None
    # default_table = Database.user_table

    # gender_table = GenderTable(collections.OrderedDict())

    def __init__(self, name="", gender=Male()):
        super(User, self).__init__()
        self.column_types[Username.column_name] = name
        # self.column_types[GenderID.column_name] = gender.genderID
        self.column_types[GenderID.column_name] = gender
        # self.column_types[
        #     GenderName.column_name] = self.gender_table.get_primary_key_value(
        #     gender)

    # def get_primary_key_value(self):
    #     db.execute(Cmd.return_matching_elements_command(self.default_table, self.name, self.gender))

    # def get_id(self):
    #     result = self.default_table.get_matching_elements(self, self.column_types)
    #     return result



# TODO: Update column_types
class DefaultClothingItem(TableElement):
    def __init__(self, gender="", clothing_item=""):
        super(DefaultClothingItem, self).__init__()
        self.column_types['gender'] = gender
        self.column_types['clothing_item'] = clothing_item


class Trip(TableElement):
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


class Gender(TableElement):
    # default_table = Database.gender_table

    def __init__(self, name=""):
        super(Gender, self).__init__()
        self.column_types[GenderName.column_name] = name

    # @classmethod
    # def get_id(cls):
    #     result = Gender.default_table.get_matching_elements(cls)
    #     return result


class Garment(TableElement):
    def __init__(self, gender, name, is_default):
        super(Garment, self).__init__()
        self.column_types[GenderName.column_name] = gender
        self.column_types[GarmentName.column_name] = name
        self.column_types[GarmentIsDefault.column_name] = is_default


class UserTripGarmentAmount(TableElement):
    pass


class UserGarmentSettings(TableElement):
    pass
