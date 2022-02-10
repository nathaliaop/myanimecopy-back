from rest_framework import serializers
from .models import Tag, Movie, Anime, Manga, Genre, Season, Episode, Chapter

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        depth = 1 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name', 'animes']
        depth = 1

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tag', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 1

class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ['id', 'tag', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 1

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'tag', 'genres', 'author', 'title', 'description', 'release_date', 'image']
        depth = 1

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'anime', 'number']

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'season', 'name', 'number']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'manga', 'name', 'number']