from pyramid.view import view_config


@view_config()
def index(request):
    return dict()
