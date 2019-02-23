from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point

from django.db.models.signals import post_save
from django.dispatch import receiver

import requests
from django.utils.http import quote_plus

from .decorators import prevent_recursion
from .services import CoworkService


class Cowork(models.Model):
    name = models.CharField(max_length=256)
    capacity = models.IntegerField()
    address = models.ForeignKey('core.Address', on_delete=models.CASCADE)
    opening_hours = models.ForeignKey('core.OpeningHours', on_delete=models.CASCADE)
    current_capacity = models.IntegerField()
    # display in app bubbles with faces of people who are currently there
    facilities = models.ForeignKey('cowork.Facilities', on_delete=models.CASCADE)
    current_coworkers = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    point = gis_models.PointField(blank=True, null=True)

    @property
    def address_query(self):
        return quote_plus(self.address.__str__())

    def get_service(self):
        return CoworkService(cowork=self)

    def save(self, *args, **kwargs):
        try:
            self.point = Point(self.address.lon, self.address.lat)
        except:
            self.point = Point(0., 0.)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MealOrder(models.Model):
    """
    Order lunch with your coworkers, connect our app
    to UberEats/whatever to make lunch ordering easy,
    besides, show a map of restaurants nearby.

    """


class Facilities(models.Model):
    dog_friendly = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    shower = models.BooleanField(default=False)
    ping_pong = models.BooleanField(default=False)
    chill_room = models.BooleanField(default=False)
    free_snack = models.BooleanField(default=False)
    conference_rooms = models.IntegerField()


@receiver(post_save, sender=Cowork, dispatch_uid="update_coords")
def get_coords_from_gis_service(instance=None, created=False,  *args, **kwargs):
    # Call gis-service pod to get coords and save them
    print("receiver")
    # if not instance.pk:
    print("instance.pk")
    full_url = "http://gis-service:9974/?address_id={}&address={}".format(instance.address.pk, instance.address_query)
    print(full_url)
    resp = requests.get(full_url)
    data = resp.json()
    print(data)
    address = instance.address
    address.lat, address.lon = data['lat'], data['lon']
    address.save(update_fields=['lat', 'lon'])
