from rest_framework import serializers
from api.models.animestatus import AnimeStatus

class AnimeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeStatus
        fields = ['id', 'favorite', 'progress', 'anime']
        depth = 3