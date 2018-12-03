#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `packit_app` package."""

import pytest
import os
from packit_app.database import Database


def test_database_connection():
    db = Database()
    assert type(db.cur) == "sqlite3.Cursor"
    assert type(db.connection) == "sqlite3.Connection"
    assert os.path.exists(Database.db_location) == True


def test_database_disconnects():
    db = Database()
    db.close_connection()
    assert db.cur.execute(
        "") == "sqlite3.ProgrammingError: Cannot operate on a closed database."
