from sqlite3 import DatabaseError


class ElementAlreadyExistsError(DatabaseError):
    """Element already exists inside table"""
    def __init__(self, *args, **kwargs):
        pass


class ElementNotFoundError(DatabaseError):
    """Element does not exists inside table"""
    def __init__(self, *args, **kwargs):
        pass


class DuplicateElementFoundError(DatabaseError):
    """More than one element with the same identifier exists in the table"""
    def __init__(self, *args, **kwargs):
        pass
