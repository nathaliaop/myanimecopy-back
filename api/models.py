from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=1000)

class Genre(models.Model):
    name = models.CharField(max_length=1000)

class Movie(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

class Anime(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

class Manga(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

class Season(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    number = models.IntegerField

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    number = models.IntegerField

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    number = models.IntegerField
