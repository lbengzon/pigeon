from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Ride(models.Model):
    date = models.DateTimeField()
    destination = models.CharField(max_length = 140)

    def get_absolute_url(self):
        return reverse("ridesharing:rideList")

    def __str__(self):
        return self.destination