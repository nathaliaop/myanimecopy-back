from rest_framework import serializers
from .models import Tag, Movie, Anime, Manga, Genre, Season, Episode, Chapter

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class GenreSerializer(serializers.ModelSerializer):
    animes = serializers.SerializerMethodField(method_name='get_animes')
    #animes = serializers.Field(source='get_animes')
    class Meta:
        model = Genre
        fields = ['id', 'name', 'animes']

    def get_animes(self, genreObj):
        queryset = Anime.objects.filter(genres__id=genreObj.id)
        return AnimeSerializer(queryset, many=True).data

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tag', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'tag', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'tag', 'genres', 'author', 'title', 'description', 'release_date', 'image']

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