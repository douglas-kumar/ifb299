from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^alter/fav/$', views.FavAlterView.as_view(), name='fav-alter'),
]
