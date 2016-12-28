from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=140, default="")
    email_address = models.EmailField(default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, default="")  # validators should be a list
    destination = models.CharField(max_length = 140)
    seats_available = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)
    date = models.DateField(default="1996-08-06")
    time = models.TimeField(default="00:00:00")

    def __str__(self):
        return self.destination

class RideRequest(models.Model):
    name = models.CharField(max_length=140, default="")
    email_address = models.EmailField(default="")
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)


