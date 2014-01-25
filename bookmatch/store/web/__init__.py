from datetime import date
from zope.interface import directlyProvides
from bookmatch.store.interfaces import (
    ISiteTop,
    IBook,
)


class SiteTop(object):
    pass


class Book(object):
    def __init__(self, title, authors, isbn, published, price):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.published = published
        self.price = price


def site_top_factory(request):
    context = SiteTop()
    directlyProvides(context, ISiteTop)
    return context


def book_factory(request):
    context = Book("あああああ", [], "978-4-00-310101-8", date(2014, 1, 1), 100000)
    directlyProvides(context, IBook)
    return context


def includeme(config):

    config.add_route("top", "/", factory=site_top_factory)
    config.add_route("book", "/books/{book_code}", factory=book_factory)
    config.scan(".views")
    config.scan(".layouts")
