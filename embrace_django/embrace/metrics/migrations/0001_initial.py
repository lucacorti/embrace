# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:26
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=1024, verbose_name='Application Id')),
                ('downloaded_at', models.DateTimeField(verbose_name='Downloaded At')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Coordinates')),
            ],
        ),
    ]
