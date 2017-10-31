from django.contrib import admin
from .models import *

# registered models to the admin interface
admin.site.register(LocationInfo)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(PublicTrans)
admin.site.register(Profile)
admin.site.register(Review)
