from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Profile from {self.user.username}'

class Social(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    followers = models.ManyToManyField(Profile, related_name='followers', blank=True)
    following = models.ManyToManyField(Profile, related_name='following', blank=True)

    def __str__(self):
        return f'Social from {self.profile.user.username}'

class Tag(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'Tag {self.name}'

class Genre(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'Genre {self.name}'

class Movie(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='movies', blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Movie {self.title}'

class Anime(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='animes', blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='animes', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Anime {self.title}'

class Manga(models.Model):
    profiles = models.ManyToManyField(Profile, related_name='mangas', blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='mangas', blank=True)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Manga {self.title}'

class Favorite(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    animes = models.ManyToManyField(Anime, related_name='animes', blank=True)
    movies = models.ManyToManyField(Movie, related_name='movies', blank=True)
    mangas = models.ManyToManyField(Manga, related_name='mangas', blank=True)

    def __str__(self):
        return f'Favorites from {self.profile.user.username}'

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name="chapters", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Chapter {self.number} from anime {self.manga.title}'

class Season(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f'Season {self.number} from anime {self.anime.title}'

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Episode {self.number} from season {self.season.number} from anime {self.anime.title}'

