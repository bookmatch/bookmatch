from zope.interface import directlyProvides
from bookmatch.store.interfaces import ISiteTop


class SiteTop(object):
    pass

def site_top_factory(request):
    context = SiteTop()
    directlyProvides(context, ISiteTop)
    return context


def includeme(config):

    config.add_route("top", "/", factory=site_top_factory)
    config.scan(".views")