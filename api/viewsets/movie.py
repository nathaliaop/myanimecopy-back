from rest_framework import viewsets
from api.models.movie import Movie
from api.serializers.movie import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()