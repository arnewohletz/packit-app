import itertools


class TableHelper:

    def __init__(self):
        pass

    def get_cursor_data_as_dictionary_generator(self, cursor) -> dict:
        """
        Converts cursor data of a table into dictionaries
        (From Python Essential Reference by David Beazley)
        :param cursor: Cursor
        :return: dict
        """

        field_names = [d[0] for d in cursor.description]
        while True:
            rows = cursor.fetchmany()
            if not rows:
                return
            for row in rows:
                yield dict(itertools.zip_longest(field_names, row))

    # TODO: Check if function is still required
    def get_row_content_as_dictionary(self, cursor) -> dict:
        """
        Converts cursor data of a single row into a dictionary
        :param cursor:
        :return: dict
        """
        field_names = [d[0] for d in cursor.description]
        while True:
            row = cursor.fetchone()
            if row is None:
                result = {}
                return result
            return dict(itertools.zip_longest(field_names, row))
