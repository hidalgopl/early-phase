class OpenStreetMapMock:

    def __init__(self, response_format="json", limit=1, polygon_svg=0):
        self.response_format = response_format
        self.limit = limit
        self.polygon_svg = polygon_svg

    def get_lat_lon(self, query):
        return 52.1, 21.2
