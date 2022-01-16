from rest_framework import serializers
from . import models

class ProviderSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Provider
    fields = "__all__"

class ParkingSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Parking
    fields = "__all__"

class ParkingPlaceSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.ParkingPlace
    fields = "__all__"