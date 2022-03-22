from django.db import models
from api.models.profile import Profile

class Social(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    followers = models.ManyToManyField(Profile, related_name='followers', blank=True)
    following = models.ManyToManyField(Profile, related_name='following', blank=True)

    def __str__(self):
        return f'Social from {self.profile.user.username}'