from rest_framework import viewsets
from api.models.movie import Movie
from api.models.anime import Anime
from api.models.manga import Manga
from api.models.genre import Genre
from api.models.chapter import Chapter
from api.models.season import Season
from api.models.episode import Episode
from api.models.profile import Profile
from api.serializers import ProfileSerializer, GenreSerializer, MovieSerializer, AnimeSerializer, MangaSerializer, ChapterSerializer, SeasonSerializer, EpisodeSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

class AnimeViewSet(viewsets.ModelViewSet):
    serializer_class = AnimeSerializer

    def get_queryset(self):
        return Anime.objects.all()

class MangaViewSet(viewsets.ModelViewSet):
    serializer_class = MangaSerializer

    def get_queryset(self):
        return Manga.objects.all()

class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.all()

class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer

    def get_queryset(self):
        return Season.objects.all()

class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.all()