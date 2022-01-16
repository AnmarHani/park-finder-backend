from . import models
from . import serializers
from Parking.serializers import ProviderSerializers
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
#----------------------------------------------
@api_view(['POST'])
def Register(request):
    serializer = serializers.UserSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      user = User.objects.get(username=serializer.data['username'], password=serializer.data['password'])
      token = Token.objects.create(user=user) 
      print(serializer.errors)

    else:
      print(serializer.errors)
    
    data = {
      'user':serializer.data,
      'Token':Token.objects.get(user=user).key,
    }
    return Response(data)

@api_view(['POST'])
def Login(request):
    is_provider = False
    username = request.data["username"]
    password = request.data["password"]

    user = User.objects.get(username=username, password=password)

    if user == None:
        print("User not exist")

    serializer = serializers.UserSerializers(user,many=False)
    provider = user.provider.all()
    if(provider.count() > 0):
      is_provider = True
    serializer2 = ProviderSerializers(provider,many=True)
    data = {
      "user":serializer.data,
      "token": Token.objects.get(user=user).key,
      "provider": serializer2.data,
      "is_provider": True if is_provider else False,
    }
    return Response(data)

@api_view(['POST'])
def Logout(request):
    request.user.auth_token.delete()
    
    data = {
      'status':'Success!'
    }
    return Response(data)
