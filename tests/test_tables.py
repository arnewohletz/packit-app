#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tables` package."""

import pytest
import os
import sqlite3

def test_each_user_has_unique_id():
    db = Database()

