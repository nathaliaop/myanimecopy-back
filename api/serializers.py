from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'release_date', 'image', 'tag']