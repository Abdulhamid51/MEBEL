from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Saved(models.Model):
    product = models.ManyToManyField(Product, related_name='saved')

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    saved = models.OneToOneField(Saved, related_name='saver', on_delete=models.CASCADE)

class 
