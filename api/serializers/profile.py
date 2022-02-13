from rest_framework import serializers
from api.models.profile import Profile
from api.serializers.animestatus import AnimeStatusSerializer
from api.serializers.mangastatus import MangaStatusSerializer
from api.serializers.moviestatus import MovieStatusSerializer

class ProfileSerializer(serializers.ModelSerializer):
    animestatus = AnimeStatusSerializer(many=True)
    mangastatus = MangaStatusSerializer(many=True)
    moviestatus = MovieStatusSerializer(many=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'animestatus', 'mangastatus', 'moviestatus', 'social']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value