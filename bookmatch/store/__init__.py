from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_mako")
    config.include(".web")
    return config.make_wsgi_app()