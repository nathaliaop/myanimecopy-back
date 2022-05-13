from rest_framework import serializers
from api.models import ChapterStatus

class ChapterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterStatus
        fields = ['id', 'progress', 'chapter']
        depth = 3