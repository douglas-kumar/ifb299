from django.db import models

# Create User table
class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    postcode = models.IntegerField()
    state = models.CharField(max_length=5)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    user_type = models.IntegerField()
    
    # How data is displayed in SQL shell
    def __unicode__(self):
        return self.first_name + " " + self.last_name + " " + self.email + " " \
               + self.phone_number + " " + self.street_number + " " \
               + self.street_name + " " + self.suburb + " " + self.postcode \
               + " " + self.state + " " + self.username + " " + self.password \
               + " " + self.user_type

# Create Item table
class Item(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    postcode = models.IntegerField()
    state = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    industry_type = models.CharField(max_length=100)
    item_type = models.IntegerField()

    # How data is displayed in SQL shell
    def __unicode__(self):
        return self.name + " " + self.phone_number + " " + self.street_number \
               + " " + self.street_name + " " + self.suburb + " " \
               + self.postcode + " " + self.state + " " + self.city + " " \
               + self.department + " " + self.industry_type + " " \
               + self.item_type
