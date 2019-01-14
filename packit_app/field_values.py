

class QueryItem:
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


class GarmentName(QueryItem):
    value = "name"


class GarmentIsDefault(QueryItem):
    value = "isDefault"


class GenderID(QueryItem):
    column_name = "genderID"


class GenderName(QueryItem):
    column_name = "gender"


class Male(QueryItem):

    def __init__(self):
        super(Male, self).__init__()
        self.genderID = 1
        self.value = "male"


class Female(QueryItem):

    def __init__(self):
        super(Female, self).__init__()
        self.genderID = 2
        self.value = "female"


class Username(QueryItem):

    def __init__(self, value):
        super(Username, self).__init__()
        self.value = value
        self.column_name = "username"


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
