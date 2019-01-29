from behave import then
from packit_app.errors import ElementAlreadyExistsError


@then(u'an error message saying that the user already exists is displayed')
def user_already_exists_error_thrown(context):
    errors = context.raised_errors
    if any(isinstance(error, ElementAlreadyExistsError) for error in errors):
        pass
    else:
        raise AssertionError("User has been created although already existing")

