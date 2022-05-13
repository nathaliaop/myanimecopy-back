from rest_framework import serializers
from api.models import Anime
from api.serializers.season import SeasonSerializer

class AnimeSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)
    class Meta:
        model = Anime
        fields = ['id', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image', 'seasons']
        depth = 2