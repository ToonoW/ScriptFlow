import collections
import copy
from uuid import uuid4

from script_flow.exceptions import FieldsRequireException
from script_flow.utils.util import json_read, json_append, json_replace
from script_flow.exceptions import ObjectNotExist, TooManyObjects


def create_id():
    return uuid4().hex


class Model(object):
    fields = None
    collection = None
    _queryset = None

    @classmethod
    def objects(cls):
        if cls._queryset is None:
            cls._queryset = QuerySet(cls)
        return cls._queryset

    def __init__(self, config):
        for var_name in ('fields', 'collection',):
            if eval('self.' + var_name) is None:
                raise ValueError(
                    'Variable {} cannot be None.'.format(var_name))

        if not isinstance(config, dict):
            raise ValueError(
                'Need object type is dict, not {}.'.format(type(config)))
        self.set_fields(self.fields)
        if not self.fields.issubset(set(config.keys())):
            raise FieldsRequireException()
        self._data = config
        self.__update_model_dict(config)

    def set_fields(self, value):
        if not isinstance(value, collections.Iterable):
            raise ValueError('Value is not iterable.')
        self.fields = set(value)

    def __update_model_dict(self, obj):
        obj = copy.copy(obj)
        if not isinstance(obj, dict):
            raise ValueError()
        obj.update(self.__dict__)
        self.__dict__ = obj


class QuerySet(object):

    def __init__(self, model):
        self._model = model
        self._collection = model.collection

    def __update_model_dict(self):
        obj = copy.copy(self._model._data)
        if not isinstance(obj, dict):
            raise ValueError()
        obj.update(self._model.__dict__)
        self._model.__dict__ = obj

    def all(self):
        items = json_read(self._collection)
        return [self._model(item) for item in items]

    def filter(self, **kwargs):
        items = self.all()
        for (key, value) in kwargs.items():
            items = filter(lambda item: item._data.get(key) == value, items)
        return items

    def get(self, **kwargs):
        items = tuple(self.filter(**kwargs))
        if len(items) == 0:
            raise ObjectNotExist()
        elif len(items) > 1:
            raise TooManyObjects()
        return items[0]

    def create(self, **kwargs):
        if not self._model.fields in kwargs.keys().append('_id'):
            raise ValueError('You must provide a mandatory fields.')
        if '_id' not in self._model.fields:
            kwargs['_id'] = create_id()
        json_append(self._collection, kwargs)

        self._model._data = kwargs

        self.__update_model_dict()
        return kwargs

    def delete(self):
        item = self.get(_id=self._model._data._id)
        data = json_read(self._collection)
        data.remove(item._data)
        json_replace(self._collection, data)
        self._model._data._id = None

    def save(self):
        item = self.get(_id=self._model._data._id)
        data = json_read(self._collection)
        data.remove(item._data)
        data.append(self._model._data)
        json_replace(self._collection, data)

        self.__update_model_dict()
