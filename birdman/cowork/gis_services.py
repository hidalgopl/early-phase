import requests
from rest_framework import status


class OpenStreetMapAPIHandler:
    base_url = "https://nominatim.openstreetmap.org/search"

    def __init__(self, response_format="json", limit=1, polygon_svg=0):
        self.response_format = response_format
        self.limit = limit
        self.polygon_svg = polygon_svg

    def get(self, query):
        full_url = self.build_full_url(query)
        response = requests.get(full_url)
        if response.status_code != status.HTTP_200_OK:
            return {}
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
"""
Decoupled databases:
POI database:
user_id | address_id | lat | lon |

Service in Go: address-updater
"""