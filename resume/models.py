from django.db import models

# Create your models here.


class Education(models.Model):
    school = models.CharField(max_length=200)
    major = models.CharField(max_length=50)
    graduation = models.DateField()
    gpa = models.FloatField()

    def __str__(self):
        return self.school


class Job(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company + ":" + self.title