from rest_framework import serializers
from .models import Tag, Movie, Anime, Manga, Genre, Chapter, Season, Episode, Profile, Favorite, Social
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'animes', 'movies', 'mangas', 'favorite', 'following', 'followers']
        depth = 3

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'profile', 'followers', 'following']
        depth = 2

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'profile', 'animes', 'movies', 'mangas']
        depth = 2

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        depth = 1 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name', 'animes', 'movies', 'mangas']
        depth = 1

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'genres', 'tag', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2

class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ['id', 'genres', 'tag', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'genres', 'tag', 'author', 'title', 'description', 'release_date', 'image']
        depth = 2

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'manga', 'name', 'number']
        depth = 1

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
