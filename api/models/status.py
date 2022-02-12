from turtle import ontimer
from django.db import models

from api.models.profile import Profile
from api.models.movie import Movie
from api.models.anime import Anime
from api.models.manga import Manga

class Status(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="status", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="status", on_delete=models.CASCADE, blank=True, null=True)
    anime = models.ForeignKey(Anime, related_name="status", on_delete=models.CASCADE, blank=True, null=True)
    manga = models.ForeignKey(Manga, related_name="status", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Status {self.number} from anime {self.anime.title}'