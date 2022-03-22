from rest_framework import serializers
from api.models.chapter import Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'number']
        depth = 2