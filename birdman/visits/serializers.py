from rest_framework import serializers

from birdman.cowork.serializers import CoWorkSerializer
from birdman.visits.models import VisitRequest


class VisitRequestSerializer(serializers.ModelSerializer):
    cowork = CoWorkSerializer()

    class Meta:
        model = VisitRequest
        fields = ('requesting_user', 'start_day', 'end_day', 'cowork', 'status')
