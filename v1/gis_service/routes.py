from aiohttp import web

import server

url_routes = [
    web.get('/', server.handle)
]