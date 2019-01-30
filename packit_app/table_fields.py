import abc


class TableField(abc.ABC):
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""

    def __init__(self):
        self.field = {}

    def get_field_as_dict(self):
        """
        Returns the column name and value of the `TableField` as a dictionary
        :return: dict
        """
        return dict({self.column_name: self.field[self.column_name]})


class TableElementField(abc.ABC):
    """
    `TableField` that is contained in a `TableElement`
    """

    def __init__(self):
        super(TableElementField, self).__init__()


class TableDataField(abc.ABC):
    """
    `TableField` that is not contained in a `TableElement`, but is assigned to
    it.

    The data of a `TableDataField` can be edited, whereas the `TableElement`
    data can only be defined during its initial creation.
    """

    def __init__(self):
        super(TableDataField, self).__init__()


class GarmentName(TableField):
    column_name = "Name"

    def __init__(self, name: str) -> None:
        super(GarmentName, self).__init__()
        self.field[self.column_name] = name


class GarmentIsDefault(TableField):
    column_name = "IsDefault"

    def __init__(self, is_default: bool) -> None:
        super(GarmentIsDefault, self).__init__()
        if is_default:
            self.field[self.column_name] = 1
        else:
            self.field[self.column_name] = 0


class GenderID(TableField):
    column_name = "GenderID"

    def __init__(self, gender_id: int) -> None:
        super(GenderID, self).__init__()
        self.field[self.column_name] = gender_id


class GenderName(TableField):
    column_name = "Name"

    def __init__(self, gender_name) -> None:
        super(GenderName, self).__init__()
        self.field[self.column_name] = gender_name


class Username(TableField):
    column_name = "Username"

    def __init__(self, username: str):
        super(Username, self).__init__()
        self.field[self.column_name] = username


class TripTemperatureDayAverage(TableField):
    column_name = "DayAverageTemp"


class TripTemperatureDayMax(TableField):
    column_name = "DayMaxTemp"


class TripTemperatureDayMin(TableField):
    column_name = "DayMinTemp"


class TripDestination(TableField):
    column_name = "Destination"


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
