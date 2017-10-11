from django.contrib import admin
from .models import *

# registered models to the admin interface
admin.site.register(locationInfo)
admin.site.register(City)
admin.site.register(Event)
admin.site.register(PublicTrans)
# admin.site.register(College)
# admin.site.register(Library)
# admin.site.register(Industries)
# admin.site.register(Hotel)
# admin.site.register(Park)
# admin.site.register(Zoo)
# admin.site.register(Museum)
# admin.site.register(Restaurant)
# admin.site.register(Mall)