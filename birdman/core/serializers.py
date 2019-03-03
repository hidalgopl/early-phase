from rest_framework import serializers

from birdman.cowork.serializers import CoWorkSerializer
from birdman.user_history.models import UserVisit


class UserVisitSerializer(serializers.ModelSerializer):
    cowork = CoWorkSerializer()

    class Meta:
        model = UserVisit
        fields = ('user', 'cowork', 'created', 'rating')
