from rest_framework.viewsets import ModelViewSet

from birdman.visits.models import VisitRequest
from birdman.visits.serializers import VisitRequestSerializer


class VisitRequestViewset(ModelViewSet):
    queryset = VisitRequest.objects.all()
    serializer_class = VisitRequestSerializer
