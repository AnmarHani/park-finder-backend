from django.contrib import admin
from . import models

admin.site.register(models.Parking)
admin.site.register(models.ParkingPlace)
admin.site.register(models.Provider)
