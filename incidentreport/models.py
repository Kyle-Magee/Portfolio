from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Report(models.Model):
    __tablename__ = 'report_logs'

    device_choices = (
        ('tablet', 'tablet'),
        ('phone', 'phone'),
        ('laptop', 'laptop'),
        ('desktop','desktop'),
        ('other', 'other'),
    )

    location_choices = (
        ('bathroom', 'bathroom'),
        ('bedroom', 'bedroom'),
        ('other', 'other')
    )

    user = models.CharField(max_length=100)
    device = models.CharField(max_length=100, choices=device_choices)
    location = models.CharField(max_length=100, choices=location_choices)
    date = models.DateField()
    time = models.TimeField(default=timezone.now())

