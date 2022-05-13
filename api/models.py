from django.db import models
from django.contrib.auth.models import User
import datetime

class Genre(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return f'Genre {self.title}'

class Anime(models.Model):
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
    genres = models.ManyToManyField(Genre, related_name='mangas', blank=True)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Manga {self.title}'

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    studio = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    release_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(default="")

    def __str__(self):
        return f'Movie {self.title}'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="")
    movies = models.ManyToManyField(Movie, through="MovieStatus")
    animes = models.ManyToManyField(Anime, through="AnimeStatus")
    mangas = models.ManyToManyField(Manga, through="MangaStatus")

    def __str__(self):
        return f'Profile from {self.user.username}'

class AnimeStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="animestatus", on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, related_name="animestatus", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Status {self.profile.user.username} from anime {self.anime.title}'

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name="chapters", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Chapter {self.number} from anime {self.manga.title}'

class MangaStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="mangastatus", on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name="mangastatus", on_delete=models.CASCADE, blank=True, null=True)
    chapters = models.ManyToManyField(Chapter, through="ChapterStatus")

    def __str__(self):
        return f'Status {self.profile.user.username} from manga {self.manga.title}'

class ChapterStatus(models.Model):
    progress = models.IntegerField()
    mangastatus = models.ForeignKey(MangaStatus, related_name="chapterstatus", on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, related_name="chapterstatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status from chapter {self.chapter.title}'

class Season(models.Model):
    anime = models.ForeignKey(Anime, related_name="seasons", on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f'Season {self.number} from anime {self.anime.title}'

class Episode(models.Model):
    season = models.ForeignKey(Season, related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    number = models.IntegerField()

    def __str__(self):
        return f'Episode {self.number} from season {self.season.number} from anime {self.anime.title}'

class SeasonStatus(models.Model):
    progress = models.IntegerField()
    animestatus = models.ForeignKey(AnimeStatus, related_name="seasonstatus", on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name="seasonstatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status from season {self.season.number} from anime {self.season.anime.title}'

class EpisodeStatus(models.Model):
    progress = models.IntegerField()
    seasonstatus = models.ForeignKey(SeasonStatus, related_name="episodestatus", on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, related_name="episodestatus", on_delete=models.CASCADE)

    def __str__(self):
        return f'Status from episode {self.episode.title}'

class MovieStatus(models.Model):
    progress = models.IntegerField()
    favorite = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name="moviestatus", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="moviestatus", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Status {self.profile.user.username} from movie {self.movie.title}'

class Social(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    followers = models.ManyToManyField(Profile, related_name='followers', blank=True)
    following = models.ManyToManyField(Profile, related_name='following', blank=True)

    def __str__(self):
        return f'Social from {self.profile.user.username}'