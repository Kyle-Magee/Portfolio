# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20170525_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 22, 55, 42, 259773, tzinfo=utc)),
        ),
    ]