from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.serializers.main import *
from main.models import Product

class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer