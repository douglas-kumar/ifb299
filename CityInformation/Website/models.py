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

    def __str__(self):
        return self.name + " " + self.state
