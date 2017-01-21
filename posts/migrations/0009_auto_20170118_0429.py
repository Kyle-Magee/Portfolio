# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 04:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170118_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='summary',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 4, 29, 3, 270943, tzinfo=utc)),
        ),
    ]
