from django.db import models
from api.models.animestatus import AnimeStatus
from api.models.season import Season

class SeasonStatus(models.Model):
    progress = models.IntegerField()
    animestatus = models.ForeignKey(AnimeStatus, related_name="seasonstatus", on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name="seasonstatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status {self.movie.title} from season {self.season.name}'