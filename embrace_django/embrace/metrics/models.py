from django.contrib.gis.db import models


class DownloadMetric(models.Model):
    app_id = models.CharField(verbose_name='Application Id', max_length=1024)
    downloaded_at = models.DateTimeField(verbose_name='Downloaded At')
    coordinates = models.PointField(verbose_name='Coordinates')
    country = models.ForeignKey('world.WorldBorder', related_name='downloads',
                                on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{o.app_id} - {o.downloaded_at}'.format(o=self)
