# from packit_app import database as db, tables
from packit_app import constants
import os
from packit_app.packit_app import Application

import parse
from behave import register_type
from packit_app.elements import Gender, User


# @parse.with_pattern(r"\w+")
# def parse_gender(gender_str: str):
#     if gender_str.lower() == "female":
#         return Female()
#     elif gender_str.lower() == "male":
#         return Male()


def before_all(context):
    # register_type(Gender=parse_gender)

    context.app = Application()
    context.db = context.app.database
    # context.user_table = context.app.user_table
    context.table_factory = context.app.table_factory
    context.user_table = context.table_factory.create_table(User())
    context.gender_table = context.table_factory.create_table(Gender())
    # context.gender_table = context.app.gender_table

    # context.db = db.Database()
    # context.table_manager = tables.TableManager()
    # context.table_factory = tables.ConcreteTableFactory()
    # context.gender_table = context.table_manager.gender_table
    # context.user_table = context.table_manager.user_table

    # context.gender_table = tables.GenderTable(elements.Gender())
    # context.input_helper = InputHelper()


def after_all(context):
    context.db.close_connection()
    os.remove(constants.DB_LOCATION)
    # os.remove('./packit.db')


def after_scenario(context, scenario):
    if 'clear_user_table_after' in scenario.tags:
        context.user_table.clean_all_content()





