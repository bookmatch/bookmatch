from pyramid.config import Configurator


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.include('pyramid_tm')
    config.include('pyramid_layout')

    config.add_mako_renderer('.html')

    config.scan('.views')
    config.scan('.layouts')
    return config.make_wsgi_app()
