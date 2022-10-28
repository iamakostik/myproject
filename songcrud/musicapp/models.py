from django.db import models


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()


class Song(models.Model):
    artiste = models.ForeignKey(Artiste)
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()


class Lyric(models.Model):
    song = models.ForeignKey(Song)
    content = models.TextField()
    song_id = models.IntegerField()