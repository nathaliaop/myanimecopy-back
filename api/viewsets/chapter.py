from rest_framework import viewsets
from api.models.chapter import Chapter
from api.serializers.chapter import ChapterSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.all()