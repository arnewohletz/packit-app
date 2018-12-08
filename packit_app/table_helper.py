import itertools


class TableHelper:

    def __init__(self):
        pass

    def get_cursor_data_as_list_of_dictionaries(self, curs) -> dict:
        """
        Converts cursor data of a table into dictionaries
        (From Python Essential Reference by David Beazley)
        :param curs: Cursor
        :return: dict
        """
        field_names = [d[0].lower() for d in curs.description]
        while True:
            rows = curs.fetchmany()
            if not rows:
                return
            for row in rows:
                yield dict(itertools.zip_longest(field_names, row))

    def get_row_content_as_dictionary(self, curs) -> dict:
        """
        Converts cursor data of a single row into a dictionary
        :param curs:
        :return: dict
        """
        field_names = [d[0].lower() for d in curs.description]
        while True:
            row = curs.fetchone()
            if row is None:
                result = {}
                return result
            return dict(itertools.zip_longest(field_names, row))
