import itertools
import abc

from .table_elements import TableElementIdentifier
from .table_fields import TableField


class StagedElement:

    def __init__(self, element: TableElementIdentifier, data: list):
        self.element = element
        self.data = data


class StagedElementContainer(abc.ABC):
    staged_elements = []

    def __init__(self):
        pass

    def stage_element(self, element: TableElementIdentifier,
                      *data: TableField):
        pass


class StagedNewUserContainer(StagedElementContainer):

    def __init__(self):
        super(StagedNewUserContainer, self).__init__()
        pass

    def stage_element(self, element: TableElementIdentifier,
                      *data: TableField) -> None:

        self.staged_elements.append(StagedElement(element, data))


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
        field_names = [d[0].lower() for d in cursor.description]
        while True:
            row = cursor.fetchone()
            if row is None:
                result = {}
                return result
            return dict(itertools.zip_longest(field_names, row))
