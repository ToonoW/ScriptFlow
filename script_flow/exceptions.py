# -*- coding: utf-8 -*-


class FieldsRequireException(ValueError):
    """Fields requirements are not fully met"""


class QuerySetException(Exception):
    """Qeury Set exception"""


class ObjectNotExist(QuerySetException):
    """Not found the object"""


class TooManyObjects(QuerySetException):
    """Too many objects returned"""
