from aiohttp import web

import logging
import peewee_async

from rest_framework import status

import config as service_config
import models
import services


class Loader:
    def __init__(self):
        self.logger = logging.getLogger(service_config.SERVICE_NAME)
        logging.basicConfig(format=service_config.LOG_FORMAT)
        models.Address.create_table(True)

        self.url_routes = [
            web.get('/', self.handle),
            web.get('/health', self.healtcheck)
        ]

    async def handle(self, request: web.Request):
        args = request.query
        objects = peewee_async.Manager(service_config.db)
        gis_service = services.CoworkService()
        lat, lon = await gis_service.get_coords(args.get('address'))
        try:
            address, created = await objects.get_or_create(models.Address, address_id=int(args.get('address_id')), lat=lat, lon=lon)
        except models.Address.DoesNotExist:
            body = {"error": "Missing address_id param"}
            return web.json_response(data=body, status=status.HTTP_400_BAD_REQUEST)
        print(address)
        if not created:
            address.lat, address.lon = lat, lon
            print(address.lat, address.lon)
            await objects.update(address)
        print(address.lat, address.lon)
        body = address.to_dict(params=['address_id', 'lat', 'lon'])
        return web.json_response(data=body)

    async def healtcheck(self, request: web.Request):
        return web.Response(text="I'm healthy!")
