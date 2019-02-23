from aiohttp import web

from loader import Loader

if __name__ == '__main__':
    loader = Loader()
    app = web.Application()
    app.add_routes(loader.url_routes)
    web.run_app(app, port=9974)
