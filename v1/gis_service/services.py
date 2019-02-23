import requests

from rest_framework import status

import mocks


class OpenStreetMapAPIHandler:
    base_url = "https://nominatim.openstreetmap.org/search"

    def __init__(self, response_format="json", limit=1, polygon_svg=0):
        self.response_format = response_format
        self.limit = limit
        self.polygon_svg = polygon_svg

    def get(self, query):
        full_url = self.build_full_url(query)
        response = requests.get(full_url)
        # logger.info(msg=full_url)
        if response.status_code != status.HTTP_200_OK:
            return {}
        # logger.info(msg=response.json())
        return response.json()[0]

    def build_full_url(self, query):
        return "{}/{}?limit={}&format={}&polygon_svg={}".format(
            self.base_url, query, self.limit, self.response_format, self.polygon_svg
        )

    def get_lat_lon(self, query):
        response = self.get(query)
        try:
            lat, lon = response["lat"], response['lon']
        except KeyError:
            return None, None
        return float(lat), float(lon)


class CoworkService:

    async def get_coords(self, address_query):
        gis_service = mocks.OpenStreetMapMock()  # mock
        lat, lon = gis_service.get_lat_lon(query=address_query)
        return lat, lon

    def update_coords(self, lat, lon):
        self.cowork.save(update_fields=[lat, lon])
