import parse

from packit_app.table_fields import Username, GarmentName
from packit_app.table_elements import Female, Male
from packit_app import table_fields as tf
from packit_app import errors


@parse.with_pattern(r"\w+")
def parse_quantity(condition: str):
    if condition == "day0to10":
        return tf.QuantityDay0To10()
    elif condition == "day10to20":
        return tf.QuantityDay10To20()
    elif condition == "dayAbove20":
        return tf.QuantityDayAbove20()
    elif condition == "dayBelow0":
        return tf.QuantityDayBelow0()
    elif condition == "dayWithSports":
        return tf.QuantitySportsDay()
    elif condition == "dayWithoutSports":
        return tf.QuantityNoSportsDay()
    elif condition == "dayInTransit":
        return tf.QuantityTransitDay()
    elif condition == "nightBelow20":
        return tf.QuantityNightBelow20()
    elif condition == "nightAbove20":
        return tf.QuantityNightAbove20()
    else:
        raise errors.UnknownConditionError


@parse.with_pattern(r"\w+")
def parse_garment_name(garment_name: str):
    return GarmentName(garment_name)


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Female()
    elif gender_str.lower() == "male":
        return Male()


@parse.with_pattern(r"\w+")
def parse_username(name: str):
    return Username(name)
