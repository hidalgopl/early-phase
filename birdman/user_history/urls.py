from django.conf.urls import url

from birdman.user_history.views import UserPastVisitsView


app_name = 'user_history'

urlpatterns = [
    url(r'past/$', UserPastVisitsView.as_view(), name='user-visits'),
]
