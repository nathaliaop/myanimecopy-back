from django.db import models
from api.models.mangastatus import MangaStatus
from api.models.chapter import Chapter

class ChapterStatus(models.Model):
    progress = models.IntegerField()
    mangastatus = models.ForeignKey(MangaStatus, related_name="chapterstatus", on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, related_name="chapterstatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status from chapter {self.chapter.title}'