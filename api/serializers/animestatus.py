from rest_framework import serializers
from api.models import AnimeStatus
from api.serializers.seasonstatus import SeasonStatusSerializer

class AnimeStatusSerializer(serializers.ModelSerializer):
    seasonstatus = SeasonStatusSerializer(many=True)
    class Meta:
        model = AnimeStatus
        fields = ['id', 'favorite', 'progress', 'anime', 'seasonstatus']
        depth = 3