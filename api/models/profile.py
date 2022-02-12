from django.db import models
from django.contrib.auth.models import User
from api.models.movie import Movie

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="")
    movies=models.ManyToManyField(Movie, through="Status")

    def __str__(self):
        return f'Profile from {self.user.username}'