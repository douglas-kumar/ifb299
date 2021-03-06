from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import inspect
from enum import Enum
from django.contrib.contenttypes.fields import GenericRelation
from fav.models import Favorite


# Models for DB migration
class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=60, decimal_places=10)
    longitude = models.DecimalField(max_digits=60, decimal_places=10)

    def __str__(self):
        return self.name + " " + self.state


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not(inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not(m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(str(p[1].value), p[0]) for p in props])
        return choices


class InfoTypes(ChoiceEnum):
    College = 0
    Library = 1
    Indusry = 2
    Hotel = 3
    Park = 4
    Zoo = 5
    Museum = 6
    Restaurant = 7
    Mall = 8


class LocationInfo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)
    phone = models.CharField(max_length=250, null=True, blank=True)
    industryType = models.CharField(max_length=500, null=True, blank=True)
    departments = models.CharField(max_length=500, null=True, blank=True)
    infoType = models.CharField(
        max_length=1,
        choices=InfoTypes.choices(),
        null=True
        )
    favorites = GenericRelation(Favorite)

    def __str__(self):
        return self.name + ' - ' + self.address


# Extend the User model for user types
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user) + " " + self.user_type


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Model for User Reviews
class Review(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    place = models.ForeignKey('LocationInfo', on_delete=models.CASCADE)
    rating = models.CharField(max_length=1)
    text = models.CharField(max_length=500)

    def __str__(self):
        return str(self.user) + " " + str(self.place) + " " + str(self.rating)

    @classmethod
    def create(cls, user, place, rating, text):
        review = cls(user=user, place=place, rating=rating, text=text)
        return review
