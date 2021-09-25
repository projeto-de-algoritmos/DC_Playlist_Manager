from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    album_image = models.CharField(max_length=100)
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.name
