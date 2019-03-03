from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .cowork.views import SearchCoworkView
from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('api/v1/', include(router.urls)),
        path('api-token-auth/', views.obtain_auth_token),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('api/v1/user_history/', include('birdman.user_history.urls', namespace='rest_history')),
        path('api/v1/visits/', include('birdman.visits.urls', namespace='visits')),

        # the 'api-root' from django rest-frameworks default router
        # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
        re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
        re_path(r'search/$', SearchCoworkView.as_view(), name='restaurant-search'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
