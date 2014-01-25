# -*- coding:utf-8 -*-
from zope.interface import Interface, Attribute


class ISiteTop(Interface):
    """ サイトトップ
    """

class IFavorite(Interface):
    """ お気に入り
    """


class ICalendar(Interface):
    """ カレンダー
    """


class IAuthor(Interface):
    """ 著者
    """


class IBook(Interface):
    """ 本
    """
    isbn = Attribute(u"ISO 2108 code (ISBN)")
    title = Attribute(u"title of book")
    authors = Attribute(u"author list of book")
    published = Attribute(u"published date of book")
    price = Attribute(u"standard price")


class INewItem(Interface):
    """ 新着
    """


class IPurchase(Interface):
    """ 購入
    """


class IPurchaseHistory(Interface):
    """ 購入履歴
    """


class IStoreUser(Interface):
    """ 利用者
    """


class Publisher(Interface):
    """ 出版社
    """


class ITopic(Interface):
    """ 特集
    """


class ICart(Interface):
    """ カート
    """


class ISearch(Interface):
    """ 検索
    """