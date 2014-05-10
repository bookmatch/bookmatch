from pyramid.view import view_config


@view_config(renderer='templates/index.html')
def index(request):
    return dict()
