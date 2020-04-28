#!/usr/bin/env python  # [package sqlite3]

"""
# pysqlite2/__init__.py: the pysqlite2 package.
#
# Copyright (C) 2005 Gerhard Häring <gh@ghaering.de>
#
# This file is part of pysqlite.
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
"""


## DATA ##

PARSE_COLNAMES = 2
# None
PARSE_DECLTYPES = 1
# None
SQLITE_ALTER_TABLE = 26
# None
SQLITE_ANALYZE = 28
# None
SQLITE_ATTACH = 24
# None
SQLITE_CREATE_INDEX = 1
# None
SQLITE_CREATE_TABLE = 2
# None
SQLITE_CREATE_TEMP_INDEX = 3
# None
SQLITE_CREATE_TEMP_TABLE = 4
# None
SQLITE_CREATE_TEMP_TRIGGER = 5
# None
SQLITE_CREATE_TEMP_VIEW = 6
# None
SQLITE_CREATE_TRIGGER = 7
# None
SQLITE_CREATE_VIEW = 8
# None
SQLITE_CREATE_VTABLE = 29
# None
SQLITE_DELETE = 9
# None
SQLITE_DENY = 1
# None
SQLITE_DETACH = 25
# None
SQLITE_DONE = 101
# None
SQLITE_DROP_INDEX = 10
# None
SQLITE_DROP_TABLE = 11
# None
SQLITE_DROP_TEMP_INDEX = 12
# None
SQLITE_DROP_TEMP_TABLE = 13
# None
SQLITE_DROP_TEMP_TRIGGER = 14
# None
SQLITE_DROP_TEMP_VIEW = 15
# None
SQLITE_DROP_TRIGGER = 16
# None
SQLITE_DROP_VIEW = 17
# None
SQLITE_DROP_VTABLE = 30
# None
SQLITE_FUNCTION = 31
# None
SQLITE_IGNORE = 2
# None
SQLITE_INSERT = 18
# None
SQLITE_OK = 0
# None
SQLITE_PRAGMA = 19
# None
SQLITE_READ = 20
# None
SQLITE_RECURSIVE = 33
# None
SQLITE_REINDEX = 27
# None
SQLITE_SAVEPOINT = 32
# None
SQLITE_SELECT = 21
# None
SQLITE_TRANSACTION = 22
# None
SQLITE_UPDATE = 23
# None
# adapters = {(<class 'datetime.date'>, <class 'sqlite3.PrepareProtocol'>): <function register_adapters_and_converters.<locals>.adapt_date>, (<class 'datetime.datetime'>, <class 'sqlite3.PrepareProtocol'>): <function register_adapters_and_converters.<locals>.adapt_datetime>}
# None
apilevel = '2.0'
# None
# converters = {'DATE': <function register_adapters_and_converters.<locals>.convert_date>, 'TIMESTAMP': <function register_adapters_and_converters.<locals>.convert_timestamp>}
# None
paramstyle = 'qmark'
# None
sqlite_version = '3.28.0'
# None
sqlite_version_info = (3, 28, 0)
# None
threadsafety = 1
# None
version = '2.6.0'
# None
version_info = (2, 6, 0)
# None


## CLASSES ##


class Cache(object):
    # Methods defined here:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    def display(*args, **kwargs):  # unknown args #
        """
        For debugging only.
        """
        raise NotImplementedError()
    
    def get(*args, **kwargs):  # unknown args #
        """
        Gets an entry from the cache or calls the factory function to produce one.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()


class Connection(object):
    """
    SQLite database connection object.
    """
    # Methods defined here:
    
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
        raise NotImplementedError()
    
    def __enter__(*args, **kwargs):  # unknown args #
        """
        For context manager. Non-standard.
        """
        raise NotImplementedError()
    
    def __exit__(*args, **kwargs):  # unknown args #
        """
        For context manager. Non-standard.
        """
        raise NotImplementedError()
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    def backup(*args, **kwargs):  # unknown args #
        """
        Makes a backup of the database. Non-standard.
        """
        raise NotImplementedError()
    
    def close(*args, **kwargs):  # unknown args #
        """
        Closes the connection.
        """
        raise NotImplementedError()
    
    def commit(*args, **kwargs):  # unknown args #
        """
        Commit the current transaction.
        """
        raise NotImplementedError()
    
    def create_aggregate(*args, **kwargs):  # unknown args #
        """
        Creates a new aggregate. Non-standard.
        """
        raise NotImplementedError()
    
    def create_collation(*args, **kwargs):  # unknown args #
        """
        Creates a collation function. Non-standard.
        """
        raise NotImplementedError()
    
    def create_function(*args, **kwargs):  # unknown args #
        """
        Creates a new function. Non-standard.
        """
        raise NotImplementedError()
    
    def cursor(*args, **kwargs):  # unknown args #
        """
        Return a cursor for the connection.
        """
        raise NotImplementedError()
    
    def execute(*args, **kwargs):  # unknown args #
        """
        Executes a SQL statement. Non-standard.
        """
        raise NotImplementedError()
    
    def executemany(*args, **kwargs):  # unknown args #
        """
        Repeatedly executes a SQL statement. Non-standard.
        """
        raise NotImplementedError()
    
    def executescript(*args, **kwargs):  # unknown args #
        """
        Executes a multiple SQL statements at once. Non-standard.
        """
        raise NotImplementedError()
    
    def interrupt(*args, **kwargs):  # unknown args #
        """
        Abort any pending database operation. Non-standard.
        """
        raise NotImplementedError()
    
    def iterdump(*args, **kwargs):  # unknown args #
        """
        Returns iterator to the dump of the database in an SQL text format. Non-standard.
        """
        raise NotImplementedError()
    
    def rollback(*args, **kwargs):  # unknown args #
        """
        Roll back the current transaction.
        """
        raise NotImplementedError()
    
    def set_authorizer(*args, **kwargs):  # unknown args #
        """
        Sets authorizer callback. Non-standard.
        """
        raise NotImplementedError()
    
    def set_progress_handler(*args, **kwargs):  # unknown args #
        """
        Sets progress handler callback. Non-standard.
        """
        raise NotImplementedError()
    
    def set_trace_callback(*args, **kwargs):  # unknown args #
        """
        Sets a trace callback called for each SQL statement (passed as unicode). Non-standard.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors defined here:
    
    DataError = None
    
    DatabaseError = None
    
    Error = None
    
    IntegrityError = None
    
    InterfaceError = None
    
    InternalError = None
    
    NotSupportedError = None
    
    OperationalError = None
    
    ProgrammingError = None
    
    Warning = None
    
    in_transaction = None
    
    isolation_level = None
    
    row_factory = None
    
    text_factory = None
    
    total_changes = None


class Cursor(object):
    """
    SQLite database cursor class.
    """
    # Methods defined here:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    def __iter__(self):
        """
        Implement iter(self).
        """
        raise NotImplementedError()
    
    def __next__(self):
        """
        Implement next(self).
        """
        raise NotImplementedError()
    
    def close(*args, **kwargs):  # unknown args #
        """
        Closes the cursor.
        """
        raise NotImplementedError()
    
    def execute(*args, **kwargs):  # unknown args #
        """
        Executes a SQL statement.
        """
        raise NotImplementedError()
    
    def executemany(*args, **kwargs):  # unknown args #
        """
        Repeatedly executes a SQL statement.
        """
        raise NotImplementedError()
    
    def executescript(*args, **kwargs):  # unknown args #
        """
        Executes a multiple SQL statements at once. Non-standard.
        """
        raise NotImplementedError()
    
    def fetchall(*args, **kwargs):  # unknown args #
        """
        Fetches all rows from the resultset.
        """
        raise NotImplementedError()
    
    def fetchmany(*args, **kwargs):  # unknown args #
        """
        Fetches several rows from the resultset.
        """
        raise NotImplementedError()
    
    def fetchone(*args, **kwargs):  # unknown args #
        """
        Fetches one row from the resultset.
        """
        raise NotImplementedError()
    
    def setinputsizes(*args, **kwargs):  # unknown args #
        """
        Required by DB-API. Does nothing in pysqlite.
        """
        raise NotImplementedError()
    
    def setoutputsize(*args, **kwargs):  # unknown args #
        """
        Required by DB-API. Does nothing in pysqlite.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors defined here:
    
    arraysize = None
    
    connection = None
    
    description = None
    
    lastrowid = None
    
    row_factory = None
    
    rowcount = None




class Error(Exception):
    """
    Common base class for all non-exit exceptions.
    """

    ## Method resolution order:
    # 1) Error
    # 2) Exception
    # 3) builtins.BaseException
    # 4) object

    # Data descriptors defined here:

    __weakref__ = None
      # list of weak references to the object (if defined)

    # --------------------------------------------------------------------
    # Methods inherited from Exception:

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Static methods inherited from Exception:

    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:

    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()

    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()

    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()

    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()

    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()

    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()

    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()

    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:

    __cause__ = None
      # exception cause

    __context__ = None
      # exception context

    __dict__ = None

    __suppress_context__ = None

    __traceback__ = None

    args = None


class DatabaseError(Error):
    """
    Common base class for all non-exit exceptions.
    """

    ## Method resolution order:
    # 1) DatabaseError
    # 2) Error
    # 3) Exception
    # 4) builtins.BaseException
    # 5) object

    # Data descriptors inherited from Error:

    __weakref__ = None
      # list of weak references to the object (if defined)

    # --------------------------------------------------------------------
    # Methods inherited from Exception:

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Static methods inherited from Exception:

    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:

    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()

    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()

    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()

    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()

    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()

    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()

    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()

    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:

    __cause__ = None
      # exception cause

    __context__ = None
      # exception context

    __dict__ = None

    __suppress_context__ = None

    __traceback__ = None

    args = None


class DataError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """

    ## Method resolution order:
    # 1) DataError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object

    # Data descriptors inherited from Error:

    __weakref__ = None
      # list of weak references to the object (if defined)

    # --------------------------------------------------------------------
    # Methods inherited from Exception:

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Static methods inherited from Exception:

    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:

    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()

    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()

    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()

    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()

    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()

    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()

    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()

    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()

    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:

    __cause__ = None
      # exception cause

    __context__ = None
      # exception context

    __dict__ = None

    __suppress_context__ = None

    __traceback__ = None

    args = None



class IntegrityError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) IntegrityError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class InterfaceError(Error):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) InterfaceError
    # 2) Error
    # 3) Exception
    # 4) builtins.BaseException
    # 5) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class InternalError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) InternalError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class NotSupportedError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) NotSupportedError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class OperationalError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) OperationalError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class PrepareProtocol(object):
    # Methods defined here:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()


class ProgrammingError(DatabaseError):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) ProgrammingError
    # 2) DatabaseError
    # 3) Error
    # 4) Exception
    # 5) builtins.BaseException
    # 6) object
    
    # Data descriptors inherited from Error:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


class Row(object):
    # Methods defined here:
    
    def __eq__(self, value):
        """
        Return self==value.
        """
        raise NotImplementedError()
    
    def __ge__(self, value):
        """
        Return self>=value.
        """
        raise NotImplementedError()
    
    def __getitem__(self, key):
        """
        Return self[key].
        """
        raise NotImplementedError()
    
    def __gt__(self, value):
        """
        Return self>value.
        """
        raise NotImplementedError()
    
    def __hash__(self):
        """
        Return hash(self).
        """
        raise NotImplementedError()
    
    def __iter__(self):
        """
        Implement iter(self).
        """
        raise NotImplementedError()
    
    def __le__(self, value):
        """
        Return self<=value.
        """
        raise NotImplementedError()
    
    def __len__(self):
        """
        Return len(self).
        """
        raise NotImplementedError()
    
    def __lt__(self, value):
        """
        Return self<value.
        """
        raise NotImplementedError()
    
    def __ne__(self, value):
        """
        Return self!=value.
        """
        raise NotImplementedError()
    
    def keys(*args, **kwargs):  # unknown args #
        """
        Returns the keys of the row.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()


class Statement(object):
    # Static methods defined here:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()


class Warning(Exception):
    """
    Common base class for all non-exit exceptions.
    """
    
    ## Method resolution order:
    # 1) Warning
    # 2) Exception
    # 3) builtins.BaseException
    # 4) object
    
    # Data descriptors defined here:
    
    __weakref__ = None
      # list of weak references to the object (if defined)
    
    # --------------------------------------------------------------------
    # Methods inherited from Exception:
    
    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Static methods inherited from Exception:
    
    def __new__(*args, **kwargs):  #  from builtins.type
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Methods inherited from builtins.BaseException:
    
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
        raise NotImplementedError()
    
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
        raise NotImplementedError()
    
    def __reduce__(*args, **kwargs):  # unknown args #
        """
        Helper for pickle.
        """
        raise NotImplementedError()
    
    def __repr__(self):
        """
        Return repr(self).
        """
        raise NotImplementedError()
    
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
        raise NotImplementedError()
    
    def __setstate__(*args, **kwargs):  # unknown args #
        raise NotImplementedError()
    
    def __str__(self):
        """
        Return str(self).
        """
        raise NotImplementedError()
    
    def with_traceback(*args, **kwargs):  # unknown args #
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """
        raise NotImplementedError()
    
    # --------------------------------------------------------------------
    # Data descriptors inherited from builtins.BaseException:
    
    __cause__ = None
      # exception cause
    
    __context__ = None
      # exception context
    
    __dict__ = None
    
    __suppress_context__ = None
    
    __traceback__ = None
    
    args = None


## FUNCTIONS ##

def adapt(*args, **kwargs):  # unknown args #
    """
    adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard.
    """
    raise NotImplementedError()

def complete_statement(*args, **kwargs):  # unknown args #
    """
    complete_statement(sql)
    
    Checks if a string contains a complete SQL statement. Non-standard.
    """
    raise NotImplementedError()

def connect(*args, **kwargs):  # unknown args #
    """
    connect(database[, timeout, detect_types, isolation_level,
            check_same_thread, factory, cached_statements, uri])
    
    Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
    """
    raise NotImplementedError()

def enable_callback_tracebacks(*args, **kwargs):  # unknown args #
    """
    enable_callback_tracebacks(flag)
    
    Enable or disable callback functions throwing errors to stderr.
    """
    raise NotImplementedError()

def enable_shared_cache(*args, **kwargs):  # unknown args #
    """
    enable_shared_cache(do_enable)
    
    Enable or disable shared cache mode for the calling thread.
    Experimental/Non-standard.
    """
    raise NotImplementedError()

def register_adapter(*args, **kwargs):  # unknown args #
    """
    register_adapter(type, callable)
    
    Registers an adapter with pysqlite's adapter registry. Non-standard.
    """
    raise NotImplementedError()

def register_converter(*args, **kwargs):  # unknown args #
    """
    register_converter(typename, callable)
    
    Registers a converter with pysqlite. Non-standard.
    """
    raise NotImplementedError()


