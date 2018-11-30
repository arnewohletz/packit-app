from behave import given, when, then

from features.support import database as database_helper
from packit_app.elements import User

helper = database_helper.DatabaseHelper()


# DEFINING STATES

@given(u'the database contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_all_elements()
    assert content == []
    print(str(content))


@given(u'the database contains a {gender} user named {name}')
def user_must_exist_after_creation(context, gender, name):
    context.user_table.clean_all_content()
    context.user = User(name=name, gender=gender)
    create_new_user(context, gender, name)
    user_does_exist(context, gender, name)


# FOR REMOVING & ADDING NEW ENTRIES

@when(u'the {gender} user named {name} is deleted')
def delete_user(context, name, gender):
    context.user = User(name=name, gender=gender)
    context.user_table.delete_element(context.user)


@when(u'a new {gender} user named {name} is created')
def create_new_user(context, gender, name):
    context.user = User(name=name, gender=gender)
    added_new_user = context.user_table.add_element(context.user)
    if not added_new_user:
        context.user_table.raised_errors.append('UserAlreadyExisting')


# FOR CHECKING ENTRIES

@then(u'the database contains a {gender} user named {name}')
def user_does_exist(context, gender, name):
    user_data = context.user_table.get_single_element(
        User(name=name, gender=gender))
    assert user_data != {}, "User does not exist in users table"
    helper.print_table(context.user_table.table_name)


@then(u'there is no {gender} user named {name} in the database')
def user_does_not_exist(context, gender, name):
    user_data = context.user_table.get_single_element(
        User(name=name, gender=gender))
    assert user_data == {}, "User is not suppose to exist in users table"
    helper.print_table(context.user_table.table_name)


@then(u'there is only one {gender} user named {name} in the database')
def user_does_exist_once(context, gender, name):
    user_does_exist(context, gender, name)
