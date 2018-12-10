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


@given(u'the default clothing set for {gender} users contains {clothes:DefaultClothes+}')
def set_gender_default_clothes(context, gender, clothes):
    raise NotImplementedError(u'STEP: Given the default clothing set for male users contains underpants, socks, tshirts, pants')


@when(u'a new male user is created')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a new male user is created')


@then(u'the new male user must specify quantities for underpants, socks, tshirts, pants')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the new male user must specify quantities for underpants, socks, tshirts, pants')


@given(u'the default clothing set for male users contains <clothing_item>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the default clothing set for male users contains <clothing_item>')


@when(u'a quantity of <quantity> is specified for <condition> condition')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a quantity of <quantity> is specified for <condition> condition')


@then(u'the new male user has a quantity of <quantity> for <clothing_item> for <condition>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the new male user has a quantity of <quantity> for <clothing_item> for <condition>')


@then(u'a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>')
