from django.contrib.gis.geos import Point

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .exceptions import NoPeerParameter
from .filters import apply_ordering
from .models import Cowork
from .serializers import CoWorkSerializer


class SearchCoworkView(ListAPIView):
    queryset = Cowork.objects.all()
    serializer_class = CoWorkSerializer
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_peer_and_user_pins(request):
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)
        if lat is None or lon is None:
            raise NoPeerParameter
        return float(lat), float(lon)

    def get_buffer(self, request):
        lat, lon = self.get_peer_and_user_pins(request)
        point = Point(lat, lon, srid=4326)
        return point

    def filter_queryset(self, queryset):
        user_buffer = self.get_buffer(self.request)
        return apply_ordering(queryset, user_buffer)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user_buffer = self.get_buffer(self.request)
        context['user_point'] = user_buffer
        return context
