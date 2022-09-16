from rest_framework import serializers
from main.models import Product, Categories, MaterialTypes, Reviews
from .accounts import UserSerializer


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialTypes
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(many=False)
    material_type = MaterialSerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Reviews
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'