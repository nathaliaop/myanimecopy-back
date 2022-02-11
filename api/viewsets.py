from rest_framework import viewsets
from .models import Tag, Genre, Movie, Anime, Manga, Chapter, Season, Episode, Profile, Favorite, Social
from api.serializers import ProfileSerializer, TagSerializer, GenreSerializer, MovieSerializer, AnimeSerializer, MangaSerializer, ChapterSerializer, SeasonSerializer, EpisodeSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()

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