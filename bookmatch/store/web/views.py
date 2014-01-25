# -*- coding:utf-8 -*-
"""
"""
from pyramid.view import view_config, view_defaults


@view_defaults(context="bookmatch.store.interfaces.ISiteTop", route_name="top")
class IndexView(object):
    """ トップ画面
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer="index.mako")
    def __call__(self):
        return dict()


class TopicView(object):
    """ 特集画面
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class NewItemView(object):
    """ 新着画面
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class AuthorView(object):
    """ 作家画面
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class SearchView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class FavoriteView(object):
    """ お気に入り
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class CartView(object):
    """ カート
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class PurchaseHistoryView(object):
    """ 販売履歴
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()


class CalendarView(object):
    """ カレンダー
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return dict()
