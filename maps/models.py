from django.db import models

# Create your models here.


class location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
