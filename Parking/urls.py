from django.urls import path
from . import views
# E = ERROR
#D = DONE
urlpatterns = [
   path('parkingPlaceIndex/<int:id>/',views.parkingPlaceIndex),#D
   path('parkingPlaceSearch/<str:name>/',views.parkingPlaceSearch),#D
   path('FreeParkingList/<int:id>/',views.freeParkingList),#D
   path('providerPlaces/<int:id>/',views.providerPlaces),#D
   path('parkingPlaceDeatils/<int:id>/',views.parkingPlaceDeatils),#D

   path('CreateParking/', views.createParking),#D 
   path('CreateProvider/', views.createProvider),#D 
   path('CreateParkingPlace/', views.createParkingPlace),#E 


   path('UpdateParkingPlace/<int:id>/', views.updateParkingPlace),#D
   path('UpdateProvider/<int:id>/', views.updateProvider),#D

   path('RentParking/<int:id>/', views.rentParking),#E
   
   path('DeleteParkingPlace/<int:id>/', views.deleteParkingPlace)#D
]