from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


class Profile(models.Model):
    GENDER = (
        ("male","MALE"),
        ("female","FEMALE"),
        ("not_set","NOT_SET")
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, default="not_set", max_length=20)
    age = models.PositiveSmallIntegerField(default=18)
    location = models.CharField(max_length=200, blank=True, null=True)
    avatar_img = models.FileField(upload_to='avatars/',blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    uid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def profile_create(sender, created, instance, *args, **kargs):
    if created == True:
        Profile.objects.create(user=instance)