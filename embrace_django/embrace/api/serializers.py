from rest_framework_json_api import serializers
from rest_framework_gis.serializers import GeometryField
from embrace.metrics.models import DownloadMetric
from embrace.world.models import WorldBorder


class DownloadMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadMetric
        fields = ['id', 'downloaded_at', 'app_id', 'coordinates']

    downloaded_at = serializers.DateTimeField()
    app_id = serializers.CharField()
    coordinates = GeometryField()


class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder
        fields = ['name', 'mpoly']

    name = serializers.CharField()
    mpoly = GeometryField()
