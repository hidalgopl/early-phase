from django.conf import settings
from django.db.models import Q
from django.utils import timezone

from geopy.distance import vincenty


def time_filter(user_buffer, queryset):
    """
    Method to check if two time ranges have at least 30 minutes common.
    """
    start_time = user_buffer.pin.start_time + timezone.timedelta(minutes=settings.MINIMUM_MEETING_LENGTH)
    end_time = user_buffer.pin.end_time - timezone.timedelta(minutes=settings.MINIMUM_MEETING_LENGTH)
    queryset = queryset.filter(Q(pin__start_time__lt=end_time) & Q(pin__end_time__gt=start_time))
    return queryset


def convert_km_to_degrees(radius):
    # TODO - more accurate calculation
    return radius * 0.008


def calculate_distance(p1, p2):
    distance = vincenty(p1.coords[::-1], p2.coords[::-1]).km
    return distance
