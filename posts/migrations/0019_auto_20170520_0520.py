# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20170520_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 20, 5, 20, 8, 794063, tzinfo=utc)),
        ),
    ]