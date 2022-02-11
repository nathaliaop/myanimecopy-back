from rest_framework import serializers
from .models import Movie, Anime, Manga, Genre, Chapter, Season, Episode, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'animes', 'movies', 'mangas', 'favorite', 'social']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'animes', 'movies', 'mangas']
        depth = 2

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'manga', 'name', 'number']
        depth = 2

class MangaSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)
    class Meta:
        model = Manga
        fields = ['id', 'genres', 'chapters', 'author', 'title', 'description', 'release_date', 'image']
        depth = 2

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'anime', 'number']
        depth = 1

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'season', 'name', 'number']
        depth = 2
