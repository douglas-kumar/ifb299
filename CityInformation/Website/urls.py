from django.conf.urls import url
from . import views

urlpatterns = [
    # /Website/
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /Website/712/
    url(r'^(?P<college_id>[0-9]+)/$', views.detail, name='detail'),
   
    # /website/brisbane
    url(r'^(?P<city_name>Brisbane)/$', views.brisbane, name='brisbane'),
    
]
