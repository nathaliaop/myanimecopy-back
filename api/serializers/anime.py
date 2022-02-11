from rest_framework import serializers
from api.models.anime import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2