from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models for DB migration
class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=60, decimal_places=10)
    longitude = models.DecimalField(max_digits=60, decimal_places=10)

    def __str__(self):
        return self.name + " " + self.state


class Event(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class PublicTrans(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class locationInfo(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)
    phone = models.CharField(max_length=250, null=True, blank=True)
    industryType = models.CharField(max_length=500, null=True, blank=True)
    departments = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


# Extend the User model for user types   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=250)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
