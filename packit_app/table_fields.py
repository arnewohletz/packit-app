import abc


class TableField(abc.ABC):
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""

    def __init__(self, value):
        self.data = {self.column_name: value}

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

    def __init__(self, value):
        super(TableElementIdentifierField, self).__init__(value)


class TableElementDataField(TableField):
    """
    `TableField` that is not contained in a `TableElement`, but is assigned to
    it.

    The data of a `TableDataField` can be edited, whereas the `TableElement`
    data can only be defined during its initial creation.
    """

    def __init__(self, value):
        super(TableElementDataField, self).__init__(value)


class GarmentID(TableElementIdentifierField):
    column_name = "GarmentID"

    def __init__(self, garment_id: int) -> None:
        super(GarmentID, self).__init__(garment_id)


class GarmentName(TableElementIdentifierField):
    column_name = "Name"

    def __init__(self, name: str) -> None:
        super(GarmentName, self).__init__(name)


class GenderID(TableElementIdentifierField):
    column_name = "GenderID"

    def __init__(self, gender_id: int) -> None:
        super(GenderID, self).__init__(gender_id)


class GenderName(TableElementIdentifierField):
    column_name = "Name"

    def __init__(self, gender_name: str) -> None:
        super(GenderName, self).__init__(gender_name)


class UserID(TableElementIdentifierField):
    column_name = "UserID"

    def __init__(self, user_id: int) -> None:
        super(UserID, self).__init__(user_id)


class Username(TableElementIdentifierField):
    column_name = "Username"

    def __init__(self, username: str):
        super(Username, self).__init__(username)


class GarmentIsDefault(TableElementDataField):
    column_name = "IsDefault"

    def __init__(self, is_default: bool = True) -> None:
        if is_default:
            super(GarmentIsDefault, self).__init__(1)
        else:
            super(GarmentIsDefault, self).__init__(0)


class QuantityDaysInTransit(TableElementDataField):
    column_name = "QuantityDayInTransit"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDaysInTransit, self).__init__(amount)


class QuantityDaysWithSports(TableElementDataField):
    column_name = "QuantityDayWithSports"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDaysWithSports, self).__init__(amount)


class QuantityDayBelowZero(TableElementDataField):
    column_name = "QuantityDayBelowZero"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDayBelowZero, self).__init__(amount)


class QuantityDayZeroToTen(TableElementDataField):
    column_name = "QuantityDayZeroToTen"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDayZeroToTen, self).__init__(amount)


class QuantityDayTenToTwenty(TableElementDataField):
    column_name = "QuantityDayTenToTwenty"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDayTenToTwenty, self).__init__(amount)


class QuantityDayAboveTwenty(TableElementDataField):
    column_name = "QuantityDayAboveTwenty"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityDayAboveTwenty, self).__init__(amount)


class QuantityNightBelowTwenty(TableElementDataField):
    column_name = "QuantityNightBelowTwenty"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityNightBelowTwenty, self).__init__(amount)


class QuantityNightAboveTwenty(TableElementDataField):
    column_name = "QuantityNightAboveTwenty"

    def __init__(self, amount: float = 1.0) -> None:
        super(QuantityNightAboveTwenty, self).__init__(amount)


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
