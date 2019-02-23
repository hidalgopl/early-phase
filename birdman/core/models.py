from django.db import models

from .validators import weekday_validator


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_created=True)
    photo_url = models.URLField()


class Address(models.Model):
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    lat = models.FloatField(verbose_name='latitude', null=True)
    lon = models.FloatField(verbose_name='longitude', null=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.address_1, self.address_2, self.city, self.country)


class OpeningHoursDaily(models.Model):
    weekday = models.IntegerField(validators=[weekday_validator, ])
    opening = models.TimeField()
    closing = models.TimeField()

    def __str__(self):
        return "{} Day: {}-{}".format(self.weekday, self.opening, self.closing)


class OpeningHours(models.Model):
    days = models.ManyToManyField('core.OpeningHoursDaily')

    def __str__(self):
        s = "Opening hours: \n"
        for day in self.days.all():
            s += day.__str__()
        return s
