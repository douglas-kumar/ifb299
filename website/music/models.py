from django.db import models
from django.core.urlresolvers import reverse

# this is the database structure

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk' : self.pk})

    # display album data
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk' : self.album.pk})

    # display song data
    def __str__(self):
        return self.song_title