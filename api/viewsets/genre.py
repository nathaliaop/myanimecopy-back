from rest_framework import viewsets
from api.models.genre import Genre
from api.serializers.genre import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()