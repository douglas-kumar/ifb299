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

class College(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    departments = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('Website:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.name + ' - ' + self.address

class Library(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Event(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class PublicTrans(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Industries(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    industryType = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Hotel(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Park(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Zoo(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Museum(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Restaurant(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

class Mall(models.Model):
    #city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.address

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
