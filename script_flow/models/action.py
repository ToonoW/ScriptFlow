# -*- coding: utf-8 -*-
from script_flow.models.base import Model
from script_flow import settings


class ActionModel(Model):

    fields = ('_id', 'name', 'action_type',)
    collection = settings.COLLECTIONS['actions']
