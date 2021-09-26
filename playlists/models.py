from django.db import models
from django.contrib.postgres.fields import ArrayField


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200)
    popularity = models.PositiveSmallIntegerField()
    duration = models.PositiveIntegerField()
    artists = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    album_image = models.CharField(max_length=200)
    playlists = models.ManyToManyField(Playlist)

    @property
    def duration_formatted(self):
        duration_milliseconds = self.duration

        seconds =(duration_milliseconds/1000)%60
        seconds = int(seconds)

        minutes = (duration_milliseconds/(1000*60))%60
        minutes = int(minutes)
        return f"{minutes}:{seconds}"

    def __str__(self):
        return self.name
