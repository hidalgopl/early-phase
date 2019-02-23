from django.contrib import admin
from .models import Address, Photo, OpeningHours, OpeningHoursDaily

admin.site.register([Address, Photo, OpeningHours, OpeningHoursDaily])