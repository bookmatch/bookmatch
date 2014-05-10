import webtest


class TestBookmatch(object):

    def test_index(self):
        from bookmatch import main
        app = main({})
        app = webtest.TestApp(app)
        res = app.get('/')
