from django.conf.urls import url
from . import views

app_name = 'Website'

urlpatterns = [
    # /Website/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /Website/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   
    # /website/brisbane
    url(r'^(?P<city_name>Brisbane)/$', views.brisbane, name='brisbane'),
    
]
