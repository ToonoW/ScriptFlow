# -*- coding: utf-8 -*-


class ViewMixin(object):
    """提供View有关的方法"""

    @property
    def geometry(self):
        return '{}x{}'.format(self.width, self.height)
