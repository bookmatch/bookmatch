import unittest
import webtest
from testfixtures import compare


class TestStore(unittest.TestCase):
    settings = {
        "mako.directories": [
            "bookmatch.store:templates",
        ]
    }

    def _makeOne(self, *args, **kwargs):
        from bookmatch.store import main
        return main(*args, **kwargs)

    def test_index(self):
        target = self._makeOne({}, **self.settings)
        app = webtest.TestApp(target)

        res = app.get("/")
        compare("hello", res.text)

    def test_book(self):
        target = self._makeOne({}, **self.settings)
        app = webtest.TestApp(target)

        res = app.get("/books/abc")