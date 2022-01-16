from . import serializers
from . import models

from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

#GET 1,2,3,4,5
@api_view(['GET'])#1
def parkingPlaceIndex(request, id):
  allParkings = models.ParkingPlace.objects.get(id=id).parking_slots.all()
  serializer = serializers.ParkingSerializers(allParkings, many = True)

  data = {
    'data' : serializer.data
  }
  return Response(data)

# @api_view(['GET'])#2
# def parkingList(request,id):
#   ParkingList = models.Parking.objects.filter(id=id)
#   serializer = serializers.ParkingSerializers(ParkingList, many = True)

#   data = {
#     'data' : serializer.data
#   }
#   return Response(data)
  
@api_view(['GET'])#3
def parkingPlaceSearch(request, name):#name
  PlacesList = models.ParkingPlace.objects.filter(name__contains=name)
  serializer = serializers.ParkingPlaceSerializers(PlacesList, many = True)

  data = {
    'data' : serializer.data
  }
  return Response(data)

@api_view(['GET'])#4
def freeParkingList(request,id):
  # FreeParks = models.Parking.objects.filter(is_available=True)
  # try:
  #   FreeParks
  #   serializer = serializers.ParkingSerializers(FreeParks, many = True)
  # except ObjectDoesNotExist:
  #   data = {
  #     "status" : "NO Parkings Available"
  #   }
  #   return Response(data)
  allFreeParkings = models.ParkingPlace.objects.get(id=id).parking_slots.filter(is_available=True)
  serializer = serializers.ParkingSerializers(allFreeParkings, many = True)

  data = {
    'data' : serializer.data
  }
  return Response(data)

#-----------------------POST/PUT------------------
@api_view(['PUT'])#ERROR
def rentParking(request, id):
  parking = models.Parking.objects.get(id=id)
  parkingSerializer = serializers.ParkingSerializers(instance=parking,data={
    'buyer_id':request.user.id, 
    'is_available':False
  })
  if parkingSerializer.is_valid():
    parkingSerializer.save()
  else:
    return Response(parkingSerializer.errors)

  return Response('Parking Slot Was Rented')


@api_view(['POST'])
def createProvider(request):
    request_data = request.data
    request_data['user_id'] = request.user.id
    providerSerializer = serializers.ProviderSerializers(data=request_data)
    if providerSerializer.is_valid():
        providerSerializer.save()
    else:
        return Response(providerSerializer.errors)

    data = {
        'data':providerSerializer.data,
    }
    return Response(data)

@api_view(['POST'])
def createParking(request):
    request_data = request.data
    request_data['user_id'] = request.user.id
    parkingSerializer = serializers.ParkingSerializers(data=request_data)
    if parkingSerializer.is_valid():
        parkingSerializer.save()
    else:
        return Response(parkingSerializer.errors)

    data = {
        'data':parkingSerializer.data,

    }
    return Response(data)

@api_view(['POST'])
def createParkingPlace(request):
    print(request.user)
    provider_id = models.Provider.objects.get(user_id=request.user.id).id
    request_data = request.data
    request_data['provider_id'] = provider_id
    parkingPlaceSerializer = serializers.ParkingPlaceSerializers(data=request_data)
    if parkingPlaceSerializer.is_valid():
      parkingPlaceSerializer.save()
      if(request.data['parking_slot_num']):
        for i in range(int(request.data['parking_slot_num'])): 
          parkingSerializers = serializers.ParkingSerializers(data = {
            "parking_location":parkingPlaceSerializer.data['place_location'], "place":parkingPlaceSerializer.data['id']
          })
          if parkingSerializers.is_valid():
            parkingSerializers.save()
          else:
            return Response(parkingSerializers.errors)
    else:
        return Response(parkingPlaceSerializer.errors)
    data = {
        'data':parkingPlaceSerializer.data,
    }
    return Response(data)

@api_view(['PUT'])
def updateParkingPlace(request, id):
    # queryset = User.objects.get(id=request.user.id) #one user
    oneParkingPlace = models.ParkingPlace.objects.get(id=id) #one user
    parkingSerializer = serializers.ParkingPlaceSerializers(instance=oneParkingPlace, data=request.data)
    if parkingSerializer.is_valid():
        parkingSerializer.save()
    else:
        return Response(parkingSerializer.errors)

    data = {
        'data':parkingSerializer.data,
    }
    return Response(data)

@api_view(['PUT'])#RESPONSE ERROR
def updateProvider(request, id):# id needed as a parameter
    provider = models.Provider.objects.get(id=id)

    providerSerializer = serializers.ProviderSerializers(instance=provider, data=request.data)
    if providerSerializer.is_valid():
      providerSerializer.save()
    else:
      return Response(providerSerializer.errors)
    data = {
        'data':providerSerializer.data,
    }
    return Response(data)
  
# ------------------------DELETE----------------------

@api_view(['DELETE'])
def deleteParkingPlace(request, id):
  parkingPlace = models.ParkingPlace.objects.get(id=id)

  try:
    parkingPlace.delete()
  except ObjectDoesNotExist:
    return Response("Object not found")

  data = "Parking deleted successfully"
  return Response(data)


  #------------------NEW_VIEW------------------------------
@api_view(['GET'])
def providerPlaces(request, id):
  provider2 = models.Provider.objects.get(id=id).places.all()
  serializer = serializers.ParkingPlaceSerializers(provider2, many = True)

  data = {
    'data' : serializer.data
  }
  return Response(data)


@api_view(['GET'])#DONE
def parkingPlaceDeatils(request, id):
  onePlace = models.ParkingPlace.objects.get(id=id)
  serializer = serializers.ParkingPlaceSerializers(onePlace, many = False)

  data = {
    'data' : serializer.data
  }
  return Response(data)