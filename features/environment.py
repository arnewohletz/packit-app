from packit_app import database as db, tables, elements
import os


def before_all(context):
    context.db = db.Database()
    context.table_factory = tables.ConcreteTableFactory()
    context.user_table = context.table_factory.create_table(elements.User())


def after_all(context):
    context.db.close_connection()
    os.remove('./packit.db')
