from django.db import models

# Create your models here.


class UserInformation(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Roles(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    relevance = models.IntegerField(default=0)

    def __str__(self):
        return self.title