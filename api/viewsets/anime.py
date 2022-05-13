from rest_framework import viewsets
from api.models import Anime
from api.serializers.anime import AnimeSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    serializer_class = AnimeSerializer

    def get_queryset(self):
        return Anime.objects.all()