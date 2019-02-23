from .gis_services import OpenStreetMapAPIHandler


class CoworkService:
    def get_coords(self, address_string):
        gis_service = OpenStreetMapAPIHandler()
        lat, lon = gis_service.get_lat_lon(query=address_string)
        return lat, lon

    def update_coords(self, lat, lon):
        self.cowork.save(update_fields=[lat, lon])
