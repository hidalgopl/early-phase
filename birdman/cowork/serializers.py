from django.utils import timezone

from rest_framework import serializers

from birdman.cowork.utils import calculate_distance

from .models import Cowork


class CoWorkSerializer(serializers.ModelSerializer):
    distance_from_user = serializers.SerializerMethodField()

    class Meta:
        model = Cowork
        exclude = ()

    def get_distance_from_user(self, obj):
        # used to display distance in mobile app
        try:
            user_point = self.context['user_point']
            return calculate_distance(user_point, obj.point)
        except KeyError:
            return None

    def get_hours(self, obj):
        current_weekday = timezone.now().strftime("%A").lower()
        if hasattr(obj, current_weekday):
            return getattr(obj, current_weekday, 'No data.')


class CoworkCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cowork
        exclude = ('point', 'lat', 'lon')