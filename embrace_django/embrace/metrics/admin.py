from django.contrib import admin

from embrace.metrics.models import DownloadMetric


@admin.register(DownloadMetric)
class DownloadMetricAdmin(admin.ModelAdmin):
    pass

