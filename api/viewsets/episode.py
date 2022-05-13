from rest_framework import viewsets
from api.models import Episode

from api.serializers.episode import EpisodeSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.all()