from behave import given, when, then, register_type
import random
import string

from features.support import database as database_helper
from features.support import custom_type_parser
from packit_app.elements import User, Male, Female, Name, Gender
from packit_app.errors import ElementAlreadyExistsError

register_type(Gender=custom_type_parser.parse_gender)

helper = database_helper.DatabaseHelper()


# DEFINING STATES

@given(u'the application contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_matching_elements()
    assert content == [], "User table was not cleared!"


@given(u'the application contains a {gender:Gender} user named {name}')
def user_must_exist_after_creation(context, gender, name):
    context.user_table.clean_all_content()
    context.user_table.add_element(User(name=name, gender=gender))
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    assert user_data != {}, "Requested user does not exist!"


# FOR REMOVING & ADDING NEW ENTRIES

@when(u'the {gender:Gender} user named {name} is deleted')
def delete_user(context, name, gender):
    context.user_table.delete_element(User(name=name, gender=gender))
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    assert user_data == {}, "User has not been deleted!"


@when(u'a new {gender:Gender} user named {name} is created')
def create_new_user(context, gender, name):
    added = context.user_table.add_element(User(name=name, gender=gender))
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    if added is True:
        assert user_data != {}, "User was supposed to be added, but wasn't."


@when(u'{amount:d} individual new users are created')
def create_multiple_random_users(context, amount: int):
    for i in range(amount):
        name = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=10))
        gender = random.choice([Male(), Female()])
        context.user_table.add_element(User(name=name, gender=gender))


@when(u'a quantity of <quantity> is assigned to all predefined clothes and conditions')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When a quantity of <quantity> is assigned to all predefined clothes and conditions')


# FOR CHECKING ENTRIES

@then(u'the application contains a {gender:Gender} user named {name}')
def user_does_exist(context, gender, name):
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    assert user_data != {}, "User does not exist in users table"


@then(u'there is no {gender:Gender} user named {name} in the application')
def user_does_not_exist(context, gender, name):
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    assert user_data == {}, "User is not suppose to exist in users table"


@then(
    u'there is only one {gender:Gender} user named {name} in the application')
def user_does_exist_once(context, gender, name):
    # user = User(name=name, gender=gender).as_dict()
    user_data = context.user_table.get_elements(User(name=name, gender=gender))
    # test = Male().as_dict()
    # context.user_table.add_element(User(name="Harry", gender=Male()))
    # context.user_table.add_element(User(name="Hank", gender=Male()))
    # user_data = context.user_table.get_elements(Male())

    # user_data = context.user_table.get_elements(User(name=name, gender=gender))
    assert len(
        user_data) == 1, "{0} user named {1} exists more than once".format(
        gender.value, name)
    # gender = context.input_helper.get_gender_element(gender)
    user_does_exist(context, gender, name)


@then(u'the application contains {amount:d} users')
def proper_amount_of_users_exists(context, amount):
    user_data = context.user_table.get_matching_elements()
    assert len(user_data) == amount


@then(
    u'a quantity of {quantity:d} is assigned for all default clothes of the {gender} user named {name}')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>')
