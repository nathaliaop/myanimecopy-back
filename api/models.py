from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=1000)


class Movie(models.Model):
#    user = models.ManyToManyField(User)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Anime(models.Model):
#    user = models.ManyToManyField(User)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Manga(models.Model):
#    user = models.ManyToManyField(User)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)