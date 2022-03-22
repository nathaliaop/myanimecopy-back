from django.db import models
from api.models.seasonstatus import SeasonStatus
from api.models.episode import Episode

class EpisodeStatus(models.Model):
    progress = models.IntegerField()
    seasonstatus = models.ForeignKey(SeasonStatus, related_name="episodestatus", on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, related_name="episodestatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status from episode {self.episode.title}'