from packit_app import database as db, tables, elements
import os


def before_all(context):
    context.db = db.Database()
    context.table_factory = tables.ConcreteTableFactory()
    context.user_table = context.table_factory.create_table(elements.User())


def after_all(context):
    context.db.close_connection()
    os.remove('./packit.db')


def after_scenario(context, scenario):
    if 'clear_user_table_after' in scenario.tags:
        context.user_table.clean_all_content()
