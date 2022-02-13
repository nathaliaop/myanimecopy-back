from rest_framework import serializers
from api.models.moviestatus import MovieStatus

class MovieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieStatus
        fields = ['id', 'favorite', 'progress', 'movie']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value