

class TableField:
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""
    value = None

    def __init__(self):
        super(TableField, self).__init__()
        self.field = {}

    def as_dict(self):
        """
        Returns the column name and value of the `TableField` as a dictionary
        :return: dict
        """
        return dict({self.column_name: self.field[self.column_name]})


class GarmentName(TableField):
    value = "Name"


class GarmentIsDefault(TableField):
    value = "IsDefault"


class GenderID(TableField):
    column_name = "GenderID"

    def __init__(self, gender_id: int):
        super(GenderID, self).__init__()
        self.field[self.column_name] = gender_id


class GenderName(TableField):
    column_name = "Name"

    def __init__(self, gender_name):
        super(GenderName, self).__init__()
        self.field[self.column_name] = gender_name


class Username(TableField):
    column_name = "Username"

    def __init__(self, name: str):
        super(Username, self).__init__()
        self.field[self.column_name] = name


class TripTemperatureDayAverage(TableField):
    column_name = "DayAverageTemp"


class TripTemperatureDayMax(TableField):
    column_name = "DayMaxTemp"


class TripTemperatureDayMin(TableField):
    column_name = "DayMinTemp"


class TripDestination(TableField):
    column_name = "Destination"

    def __init__(self, value):
        super(TripDestination, self).__init__()


class TripTemperatureNightIndoorAverage(TableField):
    column_name = "NightAverageIndoorTemp"


class TripDaysInTransit(TableField):
    column_name = "DaysInTransit"


class TripDaysWithSports(TableField):
    column_name = "DaysWithoutSports"


class TripDaysWithoutSports(TableField):
    column_name = "DaysWithSports"


class TripDateEnd(TableField):
    column_name = "EndDate"


class TripDateStart(TableField):
    column_name = "StartDate"
