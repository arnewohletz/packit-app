from behave import given, when, then, register_type

from features.support import custom_type_parser
from packit_app.table_elements import User, UserGarmentSetting, Garment
from packit_app.table_fields import UserID, UserGarmentSettingsID, GarmentID, \
    Username, GarmentName

users = []

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)
register_type(Quantity=custom_type_parser.parse_quantity)


@given(u'user {username:Username} has an entry for {garment_name:GarmentName}')
def check_user_clothing_entry_exists(context, username, garment_name):
    context.garment = Garment(context.gender_id, garment_name)
    context.username = username
    context.user_id = UserID(context.user_table.get_matching_element(
            User(username, context.gender_id))[UserID.column_name])
    context.garment_id = GarmentID(
            context.garment_table.add_element(context.garment))
    user_garment_setting_id = context.user_garment_settings_table.add_element(
            UserGarmentSetting(context.user_id, context.garment_id))
    context.user_garment_setting_id = UserGarmentSettingsID(
            user_garment_setting_id)

    result = context.user_garment_settings_table.get_matching_elements(
            context.user_garment_setting_id)

    assert len(result) == 1, "Cannot find user garment settings in the table"


@when(u'quantity for {garment_name:GarmentName} is set to '
      u'{quantity:f} for {condition:Quantity}')
def set_quantity(context, garment_name, quantity, condition):
    context.garment = Garment(context.gender_id, garment_name)
    context.user_garment_settings_table.set_data(
            context.user_garment_setting_id, condition, quantity)


@when(u'{clothing_type} is added to {gender} user {name}')
def add_singular_clothing_piece_to_user(context, clothing_type, gender, name):
    raise NotImplementedError(u'STEP: When scarf is added to user <name>')


@when(u'{clothing_type} are added to user {name}')
def add_plural_clothing_piece_to_user(context, clothing_type, name):
    raise NotImplementedError(u'STEP: When scarf is added to user <name>')


@then(u'{clothing_piece} is added to {name} with {quantity} for each '
      u'temperature')
def check_clothing_piece_quantity_all_temperatures(context, clothing_piece,
                                                   name, quantity):
    raise NotImplementedError()


@then(u'user {name:Username} has set a quantity of {value:f} {garment} '
      u'per day for {condition:Quantity}')
def check_clothing_piece_quantity_single_condition(context, name, value,
                                                   garment, condition):
    context.username = name
    context.condition = condition
    # TODO: Add a mechanism to check if context.some_variable exists
    # If not, get it via external method, otherwise keep the one existing
    result = context.user_table.get_matching_element(
            Username(context.username.field[context.username.column_name]))
    context.user_id = UserID(result[UserID.column_name])
    result = context.garment_table.get_matching_elements(GarmentName(garment),
                                                         context.gender_id)
    assert len(result) == 1, "Ambiguous results found"
    context.garment_id = GarmentID(result[0][GarmentID.column_name])

    result = context.user_garment_settings_table.get_matching_elements(
            context.user_id, context.garment_id)
    assert len(result) == 1, "Ambiguous results found"
    assert value == result[0][
        context.condition.column_name], "Incorrect quantity"
