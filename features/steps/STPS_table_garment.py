from behave import given, when, then, register_type
from features.support import custom_type_parser
from packit_app.table_elements import Garment
from packit_app.table_fields import GenderID

register_type(GarmentIsDefault=custom_type_parser.parse_default_garment)
register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)


@given(
    u'the application contains no garment type {garment:GarmentName} for {gender:Gender} users')
def specific_garment_type_does_not_exit(context, garment, gender):
    context.garment_table.clean_all_content()
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    context.garment_element = Garment(name=garment, gender_id=gender_id)

    result = context.garment_table.get_element(context.garment_element)
    assert result == [], "Garment type exists, but shouldn't."


@given(
    u'the application contains a garment type {garment:GarmentName} for {gender:Gender} users which is set as {default:GarmentIsDefault}')
def specific_garment_type_exists(context, garment, gender, default):
    specific_garment_type_is_added(context, garment=garment, gender=gender,
                                   default=default)
    specific_garment_type_has_correct_data(context, garment=garment,
                                           gender=gender, default=default)
    context.garment = garment


@when(
    u'{garment:GarmentName} is added for {gender:Gender} users as {default:GarmentIsDefault}')
def specific_garment_type_is_added(context, garment, gender, default):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    added = context.garment_table.add_element(
        Garment(gender_id=gender_id, name=garment, is_default=default))

    assert added is True, "Element was not added."


@then(
    u'the application contains {default:GarmentIsDefault} garment type {garment:GarmentName} for {gender:Gender} users')
def specific_garment_type_has_correct_data(context, default, garment, gender):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    garment_data = context.garment_table.get_matching_elements(gender_id,
                                                               garment)
    assert garment_data != [], "Garment type does not exist for specified gender"

    if len(garment_data) == 1:
        assert garment_data[0][default.column_name] == default.field[
            default.column_name]
    else:
        raise ValueError("Garment type has saved duplicates")


@when(u'the default setting is set to {default:GarmentIsDefault}')
def set_default_value(context, default):
    field = context.garment_table.get_element(context.garment_element)
    context.garment_table.set_default(data_field=field)
    raise NotImplementedError(
        u'STEP: When the default setting is set to default')
