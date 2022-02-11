from django.db import models
from api.models.manga import Manga

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name="chapters", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Chapter {self.number} from anime {self.manga.title}'