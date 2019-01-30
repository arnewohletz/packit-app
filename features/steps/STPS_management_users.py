import random
import string

from behave import given, when, then, register_type
from parse_type import TypeBuilder
from features.support import custom_type_parser, optional_word_parser
from packit_app.table_elements import User, Username, GenderID
from packit_app.errors import ElementAlreadyExistsError

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)
register_type(GarmentName=custom_type_parser.parse_garment_name)

parse_optional_word_not = TypeBuilder.with_optional(
    optional_word_parser.parse_word_not)
register_type(optional_not_=parse_optional_word_not)


# DEFINING STATES

@given(
    u'the application contains a {gender:Gender} user named {username:Username}')
def specific_user_exists(context, gender, username):
    context.user_table.clean_all_content()
    specific_user_is_added(context, gender=gender, username=username)
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    user_data = context.user_table.get_matching_elements(
        gender_id,
        username)
    assert len(user_data) == 1, "Requested user does not exist!"


@given(u'the application contains {amount:d} users')
def specific_user_quantity_exists(context, amount: int):
    for i in range(amount):
        name = Username(''.join(
            random.choices(string.ascii_lowercase + string.digits, k=10)))
        gender_id = random.choice([GenderID(1), GenderID(2)])
        context.user_table.add_element(
            User(username=name, gender_id=gender_id))
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount


@when(u'the {gender:Gender} user named {username:Username} is deleted')
def specific_user_is_deleted(context, username, gender):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    context.user_table.delete_element(
        User(username=username, gender_id=gender_id))

    user_data = context.user_table.get_matching_elements(
        gender_id,
        username)
    assert len(user_data) == 0, "User has not been deleted!"


@when(u'a new {gender:Gender} user named {username:Username} is created')
def specific_user_is_added(context, gender, username):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    try:
        added = context.user_table.add_element(
            User(username=username, gender_id=gender_id))
        user_data = context.user_table.get_matching_elements(
            gender_id,
            username)

        if added is True:
            assert len(
                user_data) == 1, "User was supposed to be added, but wasn't."

    except ElementAlreadyExistsError as error:
        context.raised_errors.append(error)


@when(u'a new {gender:Gender} user is staged for creation')
def specific_user_is_staged_for_adding(context, gender):
    raise NotImplementedError(
        u'STEP: When a new female user staged for adding')


@given(
    u'there is no {gender:Gender} user named {username:Username} in the application')
@then(
    u'there is no {gender:Gender} user named {username:Username} in the application')
def specific_user_does_not_exist(context, gender, username):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    user_data = context.user_table.get_matching_elements(
        gender_id,
        username)
    assert user_data == [], "User is not suppose to exist in users table"


@then(u'the application contains {amount:d} users')
def proper_amount_of_users_exists(context, amount):
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount


@then(
    u'the application contains a {gender:Gender} user named {username:Username}')
@then(
    u'there is only one {gender:Gender} user named {username:Username} in the application')
def specific_user_exists_only_once(context, gender, username):
    gender_id = GenderID(context.gender_table.get_primary_key_as_dict(gender))
    user_data = context.user_table.get_matching_elements(
        gender_id,
        username)
    assert len(user_data) > 0, \
        "{0} user named {1} does not exist".format(gender.value, username)
    assert len(user_data) < 2, \
        "{0} user named {1} exists more than once".format(gender.value,
                                                          username)


@then(
    u'the new user must {:optional_not_} specify quantities for {garment:GarmentName}')
def specific_garment_settings_must_be_made_when_adding_matching_user(context,
                                                                     not_,
                                                                     garment):
    raise NotImplementedError(
        u'STEP: Then the new user must specify quantities for pants')
