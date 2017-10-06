from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extend the User model for user types
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=20)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

class College(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    departments = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('Website:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.name + ' - ' + self.address

class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=60, decimal_places=10)
    longitude = models.DecimalField(max_digits=60, decimal_places=10)

    def __str__(self):
        return self.name + " " + self.state

class Library(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class PublicTrans(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Industries(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    industryType = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Park(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Zoo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Museum(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Mall(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address
    
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
