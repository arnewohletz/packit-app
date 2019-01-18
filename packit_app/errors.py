from sqlite3 import DatabaseError


class ElementAlreadyExistsError(DatabaseError):
    """Element already exists inside table"""
    def __init__(self, *args, **kwargs):
        pass
