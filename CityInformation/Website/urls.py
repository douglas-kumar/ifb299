from django.conf.urls import url
from . import views

app_name = 'Website'

urlpatterns = [
    # /Website/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    url(r'^logout/$', views.LogOut, name='logout'),

    # /Website/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /Website/Brisbane
    url(r'^(?P<city_name>Brisbane)/$', views.city_map, name='brisbane'),
   
    # /website/Sydney
    url(r'^(?P<city_name>Sydney)/$', views.city_map, name='sydney'),

    # /website/Melbourne
    url(r'^(?P<city_name>Melbourne)/$', views.city_map, name='melbourne'),

    # /website/Hobart
    url(r'^(?P<city_name>Hobart)/$', views.city_map, name='hobart'),

    # /website/Darwin
    url(r'^(?P<city_name>Darwin)/$', views.city_map, name='darwin'),

    # /website/Perth
    url(r'^(?P<city_name>Perth)/$', views.city_map, name='perth'),

    # /website/Canberra
    url(r'^(?P<city_name>Canberra)/$', views.city_map, name='canberra'),

    # /website/Adelaide
    url(r'^(?P<city_name>Adelaide)/$', views.city_map, name='adelaide'),
    
]
