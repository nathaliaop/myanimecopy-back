from rest_framework import serializers
from api.models.movie import Movie
from api.serializers.status import StatusSerializer

class MovieSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'genres', 'status', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2