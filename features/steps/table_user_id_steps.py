from behave import given, when, then


# REMOVE & ADD NEW

@when(u'{clothing_type} is added to user {name}')
def add_singular_clothing_piece_to_user(context, clothing_type, name):
    # raise NotImplementedError(u'STEP: When scarf is added to user <name>')
    print("adding new clothing piece to user...")


@when(u'{clothing_type} are added to user {name}')
def add_plural_clothing_piece_to_user(context, clothing_type, name):
    # raise NotImplementedError(u'STEP: When scarf is added to user <name>')
    print("adding new clothing piece to user...")


# (RE)SET VALUE

@when(u'quantity for {clothing_type} is set to {quantity} for each temperature')
def set_clothing_piece_quantity_all_conditions(context, clothing_type, quantity):
    print("setting clothing type quantity equally for each condition ...")


@when(u'quantity for {clothing_type} is set to {quantity} for {condition}')
def set_clothing_piece_quantity_single_condition(context, clothing_type, quantity, condition):
    print("setting quantity for clothing type for single condition ...")


# CHECK ENTRY

@given(u'user {name} has an entry for {clothing_type}')
def check_user_clothing_entry_exists(context, name, clothing_type):
    print("checking clothing type existing for that user ...")


@then(u'{clothing_piece} is added to {name} with {quantity} for each temperature')
def check_clothing_piece_quantity_all_temperatures(context, clothing_piece, name, quantity):
    print("checking clothing type quantity set equally for all conditions ...")


@then(u'user {name} has set a quantity of {quantity} for {condition}')
def check_clothing_piece_quantity_single_condition(context, name, quantity, condition):
    print("checking clothing type quantity set for single condition ...")