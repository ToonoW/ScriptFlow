# -*- coding: utf-8 -*-
from script_flow.models.base import Model
from script_flow import settings, mixin


class MainConponentModel(mixin.ViewMixin, Model):

    fields = ('_id', 'title', 'width', 'height')
    collection = settings.COLLECTIONS['main_conponents']
