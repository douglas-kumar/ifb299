from django.conf.urls import url
from . import views

# namespace for urls
app_name = 'music'

# extension to website/urls.py
urlpatterns = [

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/login/
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    # /music/<pk>/
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<album_pk>/
    url(r'album/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<album_pk>/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/song/add/
    url(r'album/song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/album/song/<song_pk>
    url(r'album/song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/album/song/<song_pk>/delete
    url(r'album/song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),
]