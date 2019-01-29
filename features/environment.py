import os
from packit_app import constants
from packit_app.packit_app import Application
from packit_app.table_elements import Gender, User, Garment


def before_all(context):
    context.app = Application()
    context.db = context.app.database
    context.raised_errors = []
    context.table_factory = context.app.table_factory
    context.user_table = context.table_factory.create_table(User())
    context.gender_table = context.table_factory.create_table(Gender())
    context.garment_table = context.table_factory.create_table(Garment())


def after_all(context):
    context.db.close_connection()
    os.remove(constants.DB_LOCATION)


def after_scenario(context, scenario):
    if 'clear_user_table_after' in scenario.tags:
        context.user_table.clean_all_content()
