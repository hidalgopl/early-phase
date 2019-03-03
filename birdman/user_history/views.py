from rest_framework.generics import ListAPIView

from birdman.core.serializers import UserVisitSerializer
from birdman.user_history.models import UserVisit


class UserPastVisitsView(ListAPIView):
    serializer_class = UserVisitSerializer

    def get_queryset(self):
        queryset = UserVisit.objects.filter(user=self.request.user).all()
        return queryset
