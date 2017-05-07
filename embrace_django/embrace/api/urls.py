from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from embrace.api.viewsets import DownloadMetricViewSet, StatsViewSet, WorldBorderViewSet

router = DefaultRouter()
router.register(r'download-metrics', DownloadMetricViewSet)
router.register(r'world-borders', WorldBorderViewSet)
router.register(r'stats', StatsViewSet, base_name='stats')
urlpatterns = router.urls
