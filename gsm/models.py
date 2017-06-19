from django.db import models

# Create your models here.


class Template(models.Model):
    template_file = models.FileField(upload_to='documents/%Y/%m/%d')

