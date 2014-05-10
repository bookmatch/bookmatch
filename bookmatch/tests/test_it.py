from pyramid import testing
from testfixtures import compare


class TestIt(object):

    def test_index(self):
        from bookmatch.views import index
        request = testing.DummyRequest()
        res = index(request)

        compare(res, dict())
