from django.db import models


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    departments = models.CharField(max_length=500)
    email = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=1000)

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



