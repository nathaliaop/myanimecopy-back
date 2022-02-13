from django.db import models

from api.models.profile import Profile
from api.models.movie import Movie

class MovieStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="moviestatus", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="moviestatus", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Status {self.profile.user.username} from movie {self.movie.title}'