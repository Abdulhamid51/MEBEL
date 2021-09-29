from django.db import models
from django.contrib.auth.models import User
from main.models import *

# Create your models here.

class Links(models.Model):
    name = models.CharField("link nomi", max_length=50)
    link = models.CharField("link", max_length=150)

    def __str__(self):
        return self.name
    

class Saved(models.Model):
    product = models.ManyToManyField(Product, related_name='saved')

    def __str__(self):
        return self.product
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_pro', on_delete=models.CASCADE)
    saved = models.OneToOneField(Saved, related_name='saver', on_delete=models.CASCADE, blank=True)
    address = models.CharField("Manzil", max_length=500,null=True, blank=True)
    phone = models.CharField('Telefon raqam', max_length=25, null=True, blank=True)
    telegram = models.CharField('telegram', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    

class ClientUser(models.Model):
    user = models.OneToOneField(User, related_name="client", on_delete=models.CASCADE)
    logo = models.ImageField("Brend logosi", upload_to='client_logos/', blank=True)
    br_name = models.CharField("Brend nomi", max_length=50)
    theme = models.CharField("rangi", max_length=50)
    link = models.CharField("linki", max_length=50, unique=True)
    rated_users = models.ManyToManyField(UserProfile, related_name="rates", blank=True)
    rates = models.PositiveIntegerField("rates", default=0)
    social_links = models.ManyToManyField(Links, related_name="client", blank=True)

    def __str__(self):
        return self.link
    