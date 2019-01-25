from packit_app.table_elements import Female, Male, Username
from packit_app.table_fields import GarmentIsDefault, GarmentName
import parse

#TODO: Adapt regex be more restrictive but accept 'non-default'
@parse.with_pattern(r"\w+.*\w+")
def parse_default_garment(default_garment: str):
    if default_garment == "default":
        return GarmentIsDefault(True)
    elif default_garment == "non-default":
        return GarmentIsDefault(False)
    else:
        raise ValueError(str(default_garment) + " is not a valid default garment descriptor")

#TODO: Adapt regex be more restrictive but accept 't-shirt'
@parse.with_pattern(r"\w+.*\w+")
def parse_garment_name(name: str):
    return GarmentName(name)


@parse.with_pattern(r"\w+")
def parse_gender(gender: str):

    if gender.lower() == "female":
        return Female()
    elif gender.lower() == "male":
        return Male()
    else:
        raise ValueError(str(gender) + " is not a valid gender description")


@parse.with_pattern(r"\w+")
def parse_username(name: str):
    return Username(name)
