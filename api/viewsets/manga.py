from rest_framework import viewsets
from api.models import Manga
from api.serializers.manga import MangaSerializer

class MangaViewSet(viewsets.ModelViewSet):
    serializer_class = MangaSerializer

    def get_queryset(self):
        return Manga.objects.all()