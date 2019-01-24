
from behave import given, when, then, register_type
from features.support import custom_type_parser

register_type(GarmentIsDefault=custom_type_parser.parse_default_garment)
register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)


@given(u'the application contains no garment type {garment:GarmentName} for {gender:Gender} users')
def step_impl(context, garment, gender):
    raise NotImplementedError(u'STEP: Given the application contains no garment type pants for male users')


@when(u'{garment:GarmentName} is added for {gender:Gender} users as {default:GarmentIsDefault}')
def step_impl(context, garment, gender, default):
    raise NotImplementedError(u'STEP: When pants is added for male users as not default')


@then(u'the application contains {default:GarmentIsDefault} garment type {garment:GarmentName} for {gender:Gender} users')
def step_impl(context, default, garment, gender):
    raise NotImplementedError(u'STEP: Then the application contains not default garment type pants for male users')
