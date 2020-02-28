from sqlite3 import DatabaseError


class AmbiguousElementError(DatabaseError):
    """More than one element matches a search pattern"""
    def __init__(self, *args, **kwargs):
        pass


class ElementAlreadyExistsError(DatabaseError):
    """Element already exists inside table"""
    def __init__(self, *args, **kwargs):
        pass


class ElementNotFoundError(DatabaseError):
    """Element does not exist in the specified table"""
    def __init__(self, *args, **kwargs):
        pass


class TableNotFoundError(DatabaseError):
    """Required table does not exist"""
    def __init__(self, *args, **kwargs):
        pass
