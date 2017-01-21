from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(null=True)
    upsides = models.TextField(null=True)
    downsides = models.TextField(null=True)
    link = models.CharField(max_length=500, null=True)
    live_link = models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return self.id

    def __str__(self):
        return self.title