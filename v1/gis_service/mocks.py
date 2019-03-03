class OpenStreetMapMock:

    def __init__(self, response_format="json", limit=1, polygon_svg=0):
        self.response_format = response_format
        self.limit = limit
        self.polygon_svg = polygon_svg

    def get_lat_lon(self, query):
        return 52.1, 21.2


async def get_or_create(self, model_, defaults=None, **kwargs):
    """Try to get an object or create it with the specified defaults.

    Return 2-tuple containing the model instance and a boolean
    indicating whether the instance was created.
    """
    class Address:
        lat = 54.3
        lon = 43.2
    return Address(), False
