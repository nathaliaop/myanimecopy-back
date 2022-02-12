from django.db import models
from django.contrib.auth.models import User
from api.models.movie import Movie
from api.models.anime import Anime
from api.models.manga import Manga

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="")
    movies = models.ManyToManyField(Movie, through="Status")
    animes = models.ManyToManyField(Anime, through="Status")
    mangas = models.ManyToManyField(Manga, through="Status")

    def __str__(self):
        return f'Profile from {self.user.username}'