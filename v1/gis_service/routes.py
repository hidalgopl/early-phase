import server
from aiohttp import web

url_routes = [
    web.get('/', server.handle)
]
