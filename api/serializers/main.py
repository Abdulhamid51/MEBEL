from rest_framework import serializers
from main.models import Product, Categories, MaterialTypes


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