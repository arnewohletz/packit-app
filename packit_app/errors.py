from sqlite3 import DatabaseError


class UserFalselyExistsError(RuntimeError):
    """ User wasn't supposed to be in database """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class UserFalselyInexistsError(RuntimeError):
    """User was supposed to be in database, but isn't"""
    def __init__(self, *args, **kwargs):
        pass


class UserAlreadyExistsError(DatabaseError):
    """ User already exists hence cannot be added"""
    def __init__(self, *args, **kwargs):
        #TODO: Add code to display alert window
        pass


class UserExistsMoreThanOnceError(DatabaseError):
    """User exists more than once"""
    def __init__(self, *args, **kwargs):
        pass


class ElementAlreadyExistsError(DatabaseError):
    """Element already exists inside table"""
    def __init__(self, *args, **kwargs):
        pass
