from rest_framework import serializers
from api.models.mangastatus import MangaStatus

class MangaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaStatus
        fields = ['id', 'favorite', 'progress', 'manga']
        depth = 3