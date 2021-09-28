from datetime import datetime

from django.db import models


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
        parsed_duration = datetime.fromtimestamp(self.duration/1000)
        minutes = parsed_duration.minute
        seconds = f"0{parsed_duration.second}" if parsed_duration.second / 10 < 1 else parsed_duration.second
        
        return f"{minutes}:{seconds}"

    def __str__(self):
        return self.name
