from behave import given, when, then, register_type
import random
import string

from features.support import database as database_helper
from features.support import custom_type_parser
from packit_app.elements import User, Male, Female, Name

register_type(Gender=custom_type_parser.parse_gender)

helper = database_helper.DatabaseHelper()


# DEFINING STATES

@given(u'the application contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_matching_elements()
    assert content == [], "User table was not cleared!"


@given(u'the application contains a {gender:Gender} user named {name}')
def users_table_contains_certain_user(context, gender, name):
    clear_users_table(context)
    create_new_user(context, gender=gender, name=name)
    user_data = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    assert len(user_data) == 1, "Requested user does not exist!"


# FOR REMOVING & ADDING NEW ENTRIES

@when(u'the {gender:Gender} user named {name} is deleted')
def delete_user(context, name, gender):
    context.user_table.delete_element(User(name=name, gender=gender))
    user_data = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    assert len(user_data) == 0, "User has not been deleted!"


@when(u'a new {gender:Gender} user named {name} is created')
def create_new_user(context, gender, name):
    added = context.user_table.add_element(User(name=name, gender=gender))
    user_data = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    if added is True:
        assert len(user_data) == 1, "User was supposed to be added, but wasn't."


@when(u'{amount:d} individual new users are created')
def create_multiple_random_users(context, amount: int):
    for i in range(amount):
        name = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=10))
        gender = random.choice([Male(), Female()])
        context.user_table.add_element(User(name=name, gender=gender))


# FOR CHECKING ENTRIES

@then(u'there is only one {gender:Gender} user named {name} in the application')
@then(u'the application contains a {gender:Gender} user named {name}')
def user_does_exist_once(context, gender, name):
    user_data = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    assert len(user_data) > 0, \
        "{0} user named {1} does not exists".format(gender.value, name)
    assert len(user_data) < 2, \
        "{0} user named {1} exists more than once".format(gender.value, name)


@then(u'there is no {gender:Gender} user named {name} in the application')
def user_does_not_exist(context, gender, name):
    user_data = context.user_table.get_matching_elements(
        User(name=name, gender=gender))
    assert user_data == [], "User is not suppose to exist in users table"


@then(u'the application contains {amount:d} users')
def proper_amount_of_users_exists(context, amount):
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount
