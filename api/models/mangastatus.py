from django.db import models

from api.models.profile import Profile
from api.models.manga import Manga
from api.models.chapter import Chapter

class MangaStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="mangastatus", on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name="mangastatus", on_delete=models.CASCADE, blank=True, null=True)
    chapters = models.ManyToManyField(Chapter, through="ChapterStatus")

    def __str__(self):
        return f'Status {self.profile.user.username} from manga {self.manga.title}'