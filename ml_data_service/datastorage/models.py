from django.db import models


# Create your models here.
class Observation(models.Model):
    feature0 = models.FloatField()
    feature1 = models.FloatField()

    category = models.IntegerField()
