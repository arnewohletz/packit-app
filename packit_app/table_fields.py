

class TableField:
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""
    value = None
    # field = {}

    def __init__(self):
        super(TableField, self).__init__()
        self.field = {}
        # self.column_name = ""
        # self.value = ""

    # TODO: Check if this function is still needed
    def as_dict(self):
        """
        Returns the column name and value as a dictionary
        :return: dict
        """
        # return dict({self.column_name: self.value})
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

#TODO: male & female were commented -> might be needed back

# class Male(TableField):
#
#     column_name = "Name"
#
#     def __init__(self):
#         super(Male, self).__init__()
#         self.field[GenderID.column_name] = 1
#         self.field[GenderName.column_name] = "male"
#     # def __init__(self):
#     #     super(Male, self).__init__()
#     #     self.GenderID = 1
#     #     self.value = "male"
#
#
# class Female(TableField):
#
#     column_name = "Name"
#
#     def __init__(self):
#         super(Female, self).__init__()
#         self.field[GenderID.column_name] = 2
#         self.field[GenderName.column_name] = "female"
#         # self.GenderID = 2
#         # self.value = "female"


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
