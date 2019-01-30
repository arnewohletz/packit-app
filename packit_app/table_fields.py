import abc


class TableField(abc.ABC):
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""

    def __init__(self):
        self.data = {}

    def get_data_as_dict(self):
        """
        Returns the column name and value of the `TableField` as a dictionary
        :return: dict
        """
        return dict({self.column_name: self.data[self.column_name]})


class TableElementIdentifierField(TableField):
    """
    `TableField` that is contained in a `TableElement`
    """

    def __init__(self):
        super(TableElementIdentifierField, self).__init__()


class TableElementDataField(TableField):
    """
    `TableField` that is not contained in a `TableElement`, but is assigned to
    it.

    The data of a `TableDataField` can be edited, whereas the `TableElement`
    data can only be defined during its initial creation.
    """

    def __init__(self):
        super(TableElementDataField, self).__init__()


class GarmentName(TableElementIdentifierField):
    column_name = "Name"

    def __init__(self, name: str) -> None:
        super(GarmentName, self).__init__()
        self.data[self.column_name] = name


class GarmentIsDefault(TableElementDataField):
    column_name = "IsDefault"

    def __init__(self, is_default: bool = True) -> None:
        super(GarmentIsDefault, self).__init__()
        if is_default:
            self.data[self.column_name] = 1
        else:
            self.data[self.column_name] = 0


class GenderID(TableElementIdentifierField):
    column_name = "GenderID"

    def __init__(self, gender_id: int) -> None:
        super(GenderID, self).__init__()
        self.data[self.column_name] = gender_id


class GenderName(TableElementIdentifierField):
    column_name = "Name"

    def __init__(self, gender_name) -> None:
        super(GenderName, self).__init__()
        self.data[self.column_name] = gender_name


class Username(TableElementIdentifierField):
    column_name = "Username"

    def __init__(self, username: str):
        super(Username, self).__init__()
        self.data[self.column_name] = username


class TripTemperatureDayAverage(TableElementDataField):
    column_name = "DayAverageTemp"


class TripTemperatureDayMax(TableElementDataField):
    column_name = "DayMaxTemp"


class TripTemperatureDayMin(TableElementDataField):
    column_name = "DayMinTemp"


class TripDestination(TableElementDataField):
    column_name = "Destination"


class TripTemperatureNightIndoorAverage(TableElementDataField):
    column_name = "NightAverageIndoorTemp"


class TripDaysInTransit(TableElementDataField):
    column_name = "DaysInTransit"


class TripDaysWithSports(TableElementDataField):
    column_name = "DaysWithoutSports"


class TripDaysWithoutSports(TableElementDataField):
    column_name = "DaysWithSports"


class TripDateEnd(TableElementDataField):
    column_name = "EndDate"


class TripDateStart(TableElementDataField):
    column_name = "StartDate"
