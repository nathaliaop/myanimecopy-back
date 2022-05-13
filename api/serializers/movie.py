from rest_framework import serializers
from api.models import Movie
from api.serializers.moviestatus import MovieStatusSerializer

class MovieSerializer(serializers.ModelSerializer):
    moviestatus = MovieStatusSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'genres', 'moviestatus', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2