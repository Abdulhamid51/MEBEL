from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.serializers.main import *
from main.models import Product, Reviews

class ProductApiView(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewCreateApiView(CreateAPIView):
    serializer_class = ReviewSerializer


class ReviewApiView(APIView):
    def get(self, request, product_id):
        queryset = Reviews.objects.filter(product_id=product_id)
        serializer_class = ReviewsSerializer(queryset, many=True)
        return Response(serializer_class.data)
