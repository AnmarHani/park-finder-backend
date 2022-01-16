from django.db import models
from django.contrib.auth.models import User


class Provider(models.Model):
  name = models.TextField(max_length=100)
  user_id = models.ForeignKey(User, related_name = "provider", on_delete=models.CASCADE)

class ParkingPlace(models.Model):
  name = models.TextField(max_length=100)#aaaaaa
  provider_id = models.ForeignKey(Provider, related_name = "places", on_delete=models.CASCADE)
  city = models.CharField(max_length=100, blank=True, null=True)
  country = models.CharField(max_length=100, blank=True, null=True)
  street = models.TextField(max_length=100, blank=True, null=True)
  place_location = models.TextField(max_length = 100) #aaa aaa
  hourly_charge = models.DecimalField(decimal_places=2, max_digits=100)

class Parking(models.Model):
  buyer_id = models.IntegerField(null=True) #5
  is_available = models.BooleanField(default=True)
  parking_location = models.TextField(max_length=100)
  place = models.ForeignKey(ParkingPlace, related_name="parking_slots", on_delete=models.CASCADE)
