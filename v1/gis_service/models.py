import peewee

from config import db


class SerializableModel:
    def to_dict(self, params):
        d = {}
        for param in params:
            if not hasattr(self, param):
                raise AttributeError("No such attribute as {}".format(param))
            d[param] = getattr(self, param)
        return d


class Address(peewee.Model, SerializableModel):
    address_id = peewee.IntegerField()
    lat = peewee.FloatField()
    lon = peewee.FloatField()

    class Meta:
        database = db
