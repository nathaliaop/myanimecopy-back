from django.db import models
from api.models.genre import Genre
import datetime

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Movie {self.title}'