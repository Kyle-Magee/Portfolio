# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 21:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20170525_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackers',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 6, 14, 21, 31, 15, 13024, tzinfo=utc)),
        ),
    ]
