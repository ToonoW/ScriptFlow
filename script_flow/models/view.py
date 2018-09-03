from script_flow.models.base import Model
from script_flow import mixin, settings


class MainViewModel(mixin.ViewMixin, Model):

    fields = ('_id', 'width', 'height', 'title')
    collection = settings.COLLECTIONS['views']
