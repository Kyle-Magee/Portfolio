# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 05:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170226_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackers',
            name='current_playtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trackers',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 5, 20, 5, 12, 9, 951327, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trackers',
            name='start_playtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trackers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TrackerUsers',
        ),
    ]
