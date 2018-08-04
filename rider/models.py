from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    longitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)


class Passenger(models.Model):
    pass_name = models.CharField(max_length=40)
    location = models.ForeignKey(Location)
    pass_pick = models.CharField(max_length=40)
    id_no = models.IntegerField(default=0)