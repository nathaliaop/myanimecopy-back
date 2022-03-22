from django.db import models
from api.models.season import Season

class Episode(models.Model):
    season = models.ForeignKey(Season, related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Episode {self.number} from season {self.season.number} from anime {self.anime.title}'

