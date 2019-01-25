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
def check_garment_type_unavailable(context, garment, gender):
    context.garment_table.clean_all_content()
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    result = context.garment_table.get_matching_elements(Garment(name=garment),
                                                         gender_id=gender_id)
    assert result == [], "Garment type exists, but shouldn't"


@when(
    u'{garment:GarmentName} is added for {gender:Gender} users as {default:GarmentIsDefault}')
def add_garment_type(context, garment, gender, default):
    # pass
    raise NotImplementedError(
        u'STEP: When pants is added for male users as not default')


@then(
    u'the application contains {default:GarmentIsDefault} garment type {garment:GarmentName} for {gender:Gender} users')
def check_garment_type_available(context, default, garment, gender):
    # pass
    raise NotImplementedError(
        u'STEP: Then the application contains not default garment type pants for male users')
