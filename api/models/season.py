from django.db import models
from api.models.anime import Anime

class Season(models.Model):
    anime = models.ForeignKey(Anime, related_name="seasons", on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f'Season {self.number} from anime {self.anime.title}'