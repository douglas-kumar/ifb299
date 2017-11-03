from django.conf.urls import include, url
from . import views

app_name = 'Website'

urlpatterns = [
    # /Website/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    url(r'^logout/$', views.LogOut, name='logout'),

    url(r'^search/$', views.Search, name='search'),

    # /Website/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /website/Brisbane
    url(r'^(?P<city_name>Brisbane)/$',
        views.CityView.as_view(), name='brisbane'),
    # /website/Sydney
    url(r'^(?P<city_name>Sydney)/$',
        views.CityView.as_view(), name='sydney'),
    # /website/Melbourne
    url(r'^(?P<city_name>Melbourne)/$',
        views.CityView.as_view(), name='melbourne'),
    # /website/Hobart
    url(r'^(?P<city_name>Hobart)/$',
        views.CityView.as_view(), name='hobart'),
    # /website/Darwin
    url(r'^(?P<city_name>Darwin)/$',
        views.CityView.as_view(), name='darwin'),
    # /website/Perth
    url(r'^(?P<city_name>Perth)/$',
        views.CityView.as_view(), name='perth'),
    # /website/Canberra
    url(r'^(?P<city_name>Canberra)/$',
        views.CityView.as_view(), name='canberra'),
    # /website/Adelaide
    url(r'^(?P<city_name>Adelaide)/$',
        views.CityView.as_view(), name='adelaide'),
]
