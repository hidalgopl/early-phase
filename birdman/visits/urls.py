from rest_framework.routers import SimpleRouter

from birdman.visits.views import VisitRequestViewset


app_name = 'visits'
router = SimpleRouter()
router.register('', VisitRequestViewset, base_name='visit_request')

urlpatterns = router.urls
