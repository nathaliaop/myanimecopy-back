from django.db import models

from api.models.profile import Profile
from api.models.movie import Movie

class Status(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    campo = models.IntegerField()

    def __str__(self):
        return f'Status {self.number} from anime {self.anime.title}'