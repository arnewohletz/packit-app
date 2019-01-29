# -*- coding: utf-8 -*-

from .database import Database
from .tables import TableFactoryImpl

"""Main module."""


class Application:

    def __init__(self):
        self.database = Database()
        self.table_factory = TableFactoryImpl(self.database)
        self.raised_errors = []
