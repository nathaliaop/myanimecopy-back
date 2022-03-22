from django.db import models

from api.models.profile import Profile
from api.models.anime import Anime

class AnimeStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="animestatus", on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name="animestatus", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Status {self.profile.user.username} from anime {self.anime.title}'