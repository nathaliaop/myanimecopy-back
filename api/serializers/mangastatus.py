from rest_framework import serializers
from api.models.mangastatus import MangaStatus
from api.serializers.chapterstatus import ChapterStatusSerializer

class MangaStatusSerializer(serializers.ModelSerializer):
    chapterstatus = ChapterStatusSerializer(many=True)
    class Meta:
        model = MangaStatus
        fields = ['id', 'favorite', 'progress', 'manga', 'chapterstatus']
        depth = 3