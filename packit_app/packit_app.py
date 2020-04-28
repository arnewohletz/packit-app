# -*- coding: utf-8 -*-

from .database import Database

"""Main module."""


class Application:

    def __init__(self):
        self.database = Database()
