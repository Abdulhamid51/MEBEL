from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.accounts import *
from accounts.models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileApiView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

import random

class LoginApiView(APIView):
    
    def get(self, request):
        code = random.randint(10000, 99999)
        username = request.data['username']
        user = User.objects.get(username=username)
        user.profile.uid = code
        user.profile.save()
        print(code)
        return Response({"code":"code sent"})

    def post(self, request):
        username = request.data['username']
        user = User.objects.get(username=username)
        key = Token.objects.get(user=user).key
        code = user.profile.uid
        
        uid = request.data['uid']
        if uid == code:
            return Response({"key":key})
        else:
            user.profile.uid = None
            user.profile.save()
            return Response({"error":"code incorrect"})
    

class RegisterApiView(APIView):
    def get(self, request):
        code = random.randint(10000, 99999)
        password = random.randint(100000,999999)
        request.data.update({"password":str(password)})
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
        username = request.data['username']
        user = User.objects.get(username=username)
        Token.objects.create(user=user)
        user.profile.uid = code
        user.profile.save()
        print(code)
        return Response({"code":"code sent", "username":username})

    def post(self, request):
        username = request.data['username']
        user = User.objects.get(username=username)
        key = Token.objects.get(user=user).key
        code = user.profile.uid
        
        uid = request.data['uid']
        if uid == code:
            return Response({"key":key})
        else:
            user.profile.uid = None
            user.profile.save()
            return Response({"error":"code incorrect"})
