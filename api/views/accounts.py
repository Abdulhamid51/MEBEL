from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.serializers.accounts import *
from accounts.models import Profile
from django.contrib.auth.models import User


class ProfileApiView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

