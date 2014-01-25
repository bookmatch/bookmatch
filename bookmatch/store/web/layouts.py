# -*- coding:utf-8 -*-
from pyramid_layout.layout import layout_config


@layout_config(template="layouts/default.mako")
class DefaultLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request