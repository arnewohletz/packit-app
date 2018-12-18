# -*- coding: utf-8 -*-

from .database import Database
from .tables import ConcreteTableFactory
from .elements import User, Gender

"""Main module."""


class Application:

    # database = None
    # user_table = None
    # gender_table = None

    def __init__(self):
        # table_factory = ConcreteTableFactory()
        self.database = Database()
        # self.user_table = table_factory.create_table(User())
        # self.gender_table = table_factory.create_table(Gender())
