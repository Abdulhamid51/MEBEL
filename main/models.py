from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.validators import MaxValueValidator, MinValueValidator


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

    rating = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveIntegerField(blank=True, null=True)
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    rate_users = models.ManyToManyField(User, blank=True)

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


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    star = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

from django.db.models import Avg
from django.http import HttpResponseForbidden

@receiver(post_save, sender=Reviews)
def update_product_star(sender, instance, created, *args, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    if instance.user in product.rate_users.all():
        instance.delete()
    else:
        product.rate_users.add(instance.user)
        product.save()
        rating = Reviews.objects.aggregate(Avg('star'))
        product.rating = float(rating['star__avg'])
        product.save()