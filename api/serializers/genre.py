from rest_framework import serializers
from api.models.genre import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title', 'animes', 'movies', 'mangas']
        depth = 2