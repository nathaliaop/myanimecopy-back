from django.db import models
from api.models.genre import Genre
import datetime

class Anime(models.Model):
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Anime {self.title}'