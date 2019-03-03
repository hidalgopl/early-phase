from django.contrib import admin

from .models import Cowork, MealOrder, Facilities

admin.site.register([Cowork, MealOrder, Facilities])
