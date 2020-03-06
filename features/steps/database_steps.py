from behave import register_type, given, when, then


@given(u'the application contains no users')
def clear_users_table(context):
    context.user_table.clean_all_content()
    content = context.user_table.get_matching_elements()
    assert content == [], "User table was not cleared!"
