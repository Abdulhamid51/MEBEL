from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    QUALITY = (
        ("ordanry","ODDIY"),
        ("midle","O'RTACHA"),
        ("good","SIFATLI"),
    )
    name = models.CharField(max_length=200)
    material_type = models.ForeignKey("main.MaterialTypes", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey("main.Categories", on_delete=models.PROTECT)
    quality = models.CharField(choices=QUALITY, max_length=20)
    info = models.TextField(blank=True)

    image = models.FileField(upload_to="product_images/base_images/")
    image1 = models.FileField(upload_to="product_images/images/")
    image2 = models.FileField(upload_to="product_images/images/")
    image3 = models.FileField(upload_to="product_images/images/")

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=150)
    icon = models.FileField(upload_to="category_icons", blank=True, null=True)

    def __str__(self):
        return self.name


class MaterialTypes(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="material_images")
    color = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name