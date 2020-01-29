from behave import given, when, then, register_type

from features.support import custom_type_parser
from packit_app.errors import ElementAlreadyExistsError
from packit_app.table_elements import User, GenderID, Garment, \
    UserGarmentSetting, GarmentName, UserID

users = []

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)


# register_type(UserGarmentSetting=custom_type_parser.parse_user_garment_setting)

# REMOVE & ADD NEW

@when(u'{clothing_type} is added to {gender} user {name}')
def add_singular_clothing_piece_to_user(context, clothing_type, gender, name):
    content = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    # content

    raise NotImplementedError(u'STEP: When scarf is added to user <name>')
    # print("adding new clothing piece to user...")


@when(u'{clothing_type} are added to user {name}')
def add_plural_clothing_piece_to_user(context, clothing_type, name):
    raise NotImplementedError(u'STEP: When scarf is added to user <name>')


# (RE)SET VALUE

@when(
    u'quantity for {clothing_type} is set to {quantity} for each temperature')
def set_clothing_piece_quantity_all_conditions(context, clothing_type,
                                               quantity):
    # print("setting clothing type quantity equally for each condition ...")
    raise NotImplementedError()


@when(u'quantity for {clothing_type} is set to {quantity} for {condition}')
def set_clothing_piece_quantity_single_condition(context, clothing_type,
                                                 quantity, condition):
    # print("setting quantity for clothing type for single condition ...")
    raise NotImplementedError()


# CHECK ENTRY

# @given(
#     u'user {username:Username} has an entry for {garment:UserGarmentSetting}')
@given(
    u'user {username:Username} has an entry for {garment:GarmentName}')
def check_user_clothing_entry_exists(context, username, garment):
    # print("checking clothing type existing for that user ...")
    context.garment = Garment(context.gender_id, garment.get_value())
    context.user_id = UserID(context.user_table.get_matching_element(
        User(username, context.gender_id))[UserID.column_name])
    context.garment_id = context.garment_table.add_element(context.garment)
    context.user_garment_setting = context.user_garment_settings_table.add_element(
        UserGarmentSetting(context.user_id, context.garment_id))

    context.garment_setting_id = context.user_garment_settings_table.add_elementcontext.user_id

    context.user_garment_settings_table.add_element(garment)
    # user = User(username=name, gender_id=)
    raise NotImplementedError()


@then(
    u'{clothing_piece} is added to {name} with {quantity} for each temperature')
def check_clothing_piece_quantity_all_temperatures(context, clothing_piece,
                                                   name, quantity):
    # print("checking clothing type quantity set equally for all conditions ...")
    raise NotImplementedError()


@then(u'user {name} has set a quantity of {quantity} for {condition}')
def check_clothing_piece_quantity_single_condition(context, name, quantity,
                                                   condition):
    # print("checking clothing type quantity set for single condition ...")
    raise NotImplementedError()
