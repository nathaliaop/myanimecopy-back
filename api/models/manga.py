from django.db import models
from api.models.profile import Profile
from api.models.genre import Genre
import datetime

class Manga(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='mangas', blank=True)
    genres = models.ManyToManyField(Genre, related_name='mangas', blank=True)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Manga {self.title}'