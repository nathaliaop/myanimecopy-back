from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'Genre {self.name}'