from rest_framework import serializers
from api.models import Manga
from api.serializers.chapter import ChapterSerializer

class MangaSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)
    class Meta:
        model = Manga
        fields = ['id', 'genres', 'chapters', 'author', 'title', 'description', 'release_date', 'image']
        depth = 2