from behave import register_type, given, when, then
from parse_type import TypeBuilder
import parse

default_clothing_pieces = ["underpants", "socks", "pants", "tshirts"]
extra_female_default_clothing_pieces = ["bra"]

for elem in extra_female_default_clothing_pieces:
    default_clothing_pieces.append(elem)

all_default_clothing_pieces = default_clothing_pieces


@parse.with_pattern(r"\w+")
def parse_clothes(text):
    return str(text)


parse_default_clothes = TypeBuilder.with_one_or_more(parse_clothes,
                                                     listsep=",")
type_dict = {"DefaultClothes+": parse_default_clothes}
register_type(**type_dict)


@then(
    u'the {gender} user named {name} has presettings for {clothes:DefaultClothes+}')
def check_settings(context, gender, name, clothes):
    print("Checking default clothes...")
    # raise NotImplementedError(u'STEP: Then the male user named Harry has presettings for underpants, socks, tshirts and pants')
