from django.conf.urls import url

from .views import SearchCoworkView

urlpatterns = [
    url(r'search/$', SearchCoworkView.as_view(), name='restaurant-search'),
]
