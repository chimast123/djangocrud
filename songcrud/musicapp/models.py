from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Song(models.Model):
    title = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=400)

class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=400) 