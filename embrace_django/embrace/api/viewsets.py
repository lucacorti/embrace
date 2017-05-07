from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from embrace.api.serializers import DownloadMetricSerializer, WorldBorderSerializer

from embrace.metrics.models import DownloadMetric
from embrace.world.models import WorldBorder


class DownloadMetricViewSet(ModelViewSet):
    model = DownloadMetric
    queryset = DownloadMetric.objects.all().order_by('-downloaded_at')
    serializer_class = DownloadMetricSerializer

    def perform_create(self, serializer):
        metric = serializer.save()
        metric.country = WorldBorder.objects.filter(
            mpoly__contains=metric.coordinates
        ).first()
        metric.save()


class WorldBorderViewSet(ModelViewSet):
    model = WorldBorder
    queryset = WorldBorder.objects.all().order_by('-name')
    serializer_class = WorldBorderSerializer


class StatsViewSet(ViewSet):

    def list(self, request):
        metrics = DownloadMetric.objects.all()

        times = [
            ('morning', 6, 12),
            ('afternoon', 12, 18),
            ('evening', 18, 24),
            ('night', 24, 6)
        ]

        time_metrics = [{
            'label': label.capitalize(),
            'value': metrics.filter(
                downloaded_at__hour__gte=min_hour, downloaded_at__hour__lt=max_hour
        ).count()} for (label, min_hour, max_hour) in times]

        country_metrics = [{
            'label': country.name,
            'value': country.downloads__count
        } for country in WorldBorder.objects.annotate(Count('downloads')).filter(
            downloads__count__gte=1
        ).order_by('-downloads__count')]

        app_metrics = []
        for data in DownloadMetric.objects.values('app_id').distinct():
            app_id = data.get('app_id')
            app_metrics.append({
                'label': app_id,
                'value': DownloadMetric.objects.filter(app_id=app_id).count()
            })

        return Response({
            'by_time': time_metrics,
            'by_country': country_metrics,
            'by_app': app_metrics
        })
