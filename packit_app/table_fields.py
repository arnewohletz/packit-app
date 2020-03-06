import abc


class TableField(abc.ABC):
    """
    A TableField represents a single field inside a table.

    Each TableField type holds the the column name it is saved in as well as
    its value.
    """

    column_name = ""

    def __init__(self, value):
        self.field = {self.column_name: value}

    def get_as_dict(self):
        """
        Returns the column name and value of the `TableField` as a dictionary
        :return: dict
        """
        return self.field

    def get_value(self):
        """
        Returns the field value as a string
        :return: str
        """
        return self.field[self.column_name]

    def set_value(self, value):
        """
        Sets the value of the table field
        :rtype None
        """
        self.field[self.column_name] = value


# class ConditionalQuantityFactory(abc.ABC):
#
#     @abstractmethod
#     def create_conditional_quantity(self, value: int, condition: Condition):
#         pass
#
#
#
class Condition:
    pass


class Day0To10(Condition):
    pass


class Day10To20(Condition):
    pass


class ConditionalQuantity(TableField):
    pass


class ConditionalQuantityFactory:

    def create_conditional_quantity(self, value: int, condition: Condition):
        if isinstance(condition, Day10To20):
            return QuantityDay10To20(value)
        elif isinstance(condition, Day0To10):
            return QuantityDay0To10(value)


class TableDataField(TableField):

    def __init__(self, value):
        super(TableDataField, self).__init__(value)


class TableIdentifierField(TableField):

    def __init__(self, value):
        super(TableIdentifierField, self).__init__(value)


class GarmentID(TableIdentifierField):
    column_name = "GarmentID"

    def __init__(self, garment_id: int = 1):
        super(GarmentID, self).__init__(garment_id)


class GarmentIsDefault(TableDataField):
    column_name = "IsDefault"

    def __init__(self, is_default: bool = False):
        super(GarmentIsDefault, self).__init__(is_default)


class GarmentName(TableIdentifierField):
    column_name = "Name"

    def __init__(self, garment_name: str = ""):
        super(GarmentName, self).__init__(garment_name)


class GenderID(TableIdentifierField):
    column_name = "GenderID"

    def __init__(self, gender_id: int = 1):
        super(GenderID, self).__init__(gender_id)


class GenderName(TableIdentifierField):
    column_name = "Name"

    def __init__(self, gender_name):
        super(GenderName, self).__init__(gender_name)


class Quantity(TableDataField):

    def __init__(self, quantity=0.0):
        super(Quantity, self).__init__(quantity)


class QuantityDay0To10(Quantity):
    column_name = "QuantityDay0To10"


class QuantityDay10To20(Quantity):
    column_name = "QuantityDay10To20"


class QuantityDayBelow0(Quantity):
    column_name = "QuantityDayBelow0"


class QuantityDayAbove20(Quantity):
    column_name = "QuantityDayAbove20"


class QuantitySportsDay(Quantity):
    column_name = "QuantitySportsDay"


class QuantityNoSportsDay(Quantity):
    column_name = "QuantityNoSportsDay"


class QuantityTransitDay(Quantity):
    column_name = "QuantityTransitDay"


class QuantityNightBelow20(Quantity):
    column_name = "QuantityNightBelow20"


class QuantityNightAbove20(Quantity):
    column_name = "QuantityNightAbove20"


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


class UserGarmentSettingsID(TableIdentifierField):
    column_name = "GarmentSettingsID"

    def __init__(self, user_garment_settings_id: int):
        super(UserGarmentSettingsID, self).__init__(user_garment_settings_id)


class UserID(TableIdentifierField):
    column_name = "UserID"

    def __init__(self, user_id: int = 1):
        super(UserID, self).__init__(user_id)


class Username(TableIdentifierField):
    column_name = "Username"

    def __init__(self, username: str):
        super(Username, self).__init__(username)
