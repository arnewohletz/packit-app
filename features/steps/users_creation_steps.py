import random
import string

from behave import given, when, then, register_type
from features.support import database as database_helper
from features.support import custom_type_parser
from packit_app.table_elements import User, Username, GenderID, UserID

register_type(Gender=custom_type_parser.parse_gender)
register_type(Username=custom_type_parser.parse_username)

helper = database_helper.DatabaseHelper()


# DEFINING STATES

@given(u'the application contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_matching_elements()
    assert content == [], "User table was not cleared!"


@given(
    u'the application contains a {gender:Gender} user named {username:Username}')
def users_table_contains_certain_user(context, gender, username):
    clear_users_table(context)
    create_new_user(context, gender=gender, username=username)
    gender_id = GenderID(context.gender_table.get_primary_key(gender))
    user_data = context.user_table.get_matching_elements(gender_id, username)
    assert len(user_data) == 1, "Requested user does not exist!"

    context.username = username
    context.gender_id = gender_id
    context.user_id = UserID(context.user_table.get_primary_key(
        User(username, gender_id)))
    # TODO: Fix this method call
    # Problem: GenderID object must receive an integer value, but previously
    # received a dictionary
    # Fix: variables must be more clear, from which type they are (GOOD) OR
    # make app less sensitive to type of a table object is (BEST)


# FOR REMOVING & ADDING NEW ENTRIES

@when(u'the {gender:Gender} user named {username:Username} is deleted')
def delete_user(context, username, gender):
    gender_id = context.gender_table.get_primary_key(gender)
    context.user_table.delete_element(
        User(username=username, gender_id=GenderID(gender_id)))
    user_data = context.user_table.get_matching_elements(
        GenderID(gender_id), username)
    assert len(user_data) == 0, "User has not been deleted!"


@when(u'a new {gender:Gender} user named {username:Username} is created')
def create_new_user(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    added = context.user_table.add_element(
        User(username=username, gender_id=GenderID(gender_id)))

    user_data = context.user_table.get_matching_elements(
        username, GenderID(gender_id))
    if added is True:
        assert len(
            user_data) == 1, "User was supposed to be added, but wasn't."


@when(u'{amount:d} individual new users are created')
def create_multiple_random_users(context, amount: int):
    for i in range(amount):
        name = Username(''.join(
            random.choices(string.ascii_lowercase + string.digits, k=10)))
        gender_id = random.choice([GenderID(1), GenderID(2)])
        context.user_table.add_element(
            User(username=name, gender_id=gender_id))


# FOR CHECKING ENTRIES

@then(
    u'there is only one {gender:Gender} user named {username:Username} in the application')
@then(
    u'the application contains a {gender:Gender} user named {username:Username}')
def user_does_exist_once(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    user_data = context.user_table.get_matching_elements(
        GenderID(gender_id), username)
    assert len(user_data) > 0, \
        "{0} user named {1} does not exists".format(gender.value, username)
    assert len(user_data) < 2, \
        "{0} user named {1} exists more than once".format(gender.value,
                                                          username)


@then(
    u'there is no {gender:Gender} user named {username:Username} in the application')
def user_does_not_exist(context, gender, username):
    gender_id = context.gender_table.get_primary_key(gender)
    user_data = context.user_table.get_matching_elements(
        GenderID(gender_id), username)
    assert user_data == [], "User is not suppose to exist in users table"


@then(u'the application contains {amount:d} users')
def proper_amount_of_users_exists(context, amount):
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount
