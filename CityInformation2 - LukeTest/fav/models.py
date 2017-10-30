from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (
    GenericForeignKey)
from django.contrib.contenttypes.models import ContentType


class Favorite(models.Model):

    """ Represents an instance of Favorite """

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, null=True, blank=True)
    cookie = models.CharField(null=True, max_length=256, blank=True)
