from rest_framework import serializers
from api.models import Profile
from api.serializers.animestatus import AnimeStatusSerializer
from api.serializers.mangastatus import MangaStatusSerializer
from api.serializers.moviestatus import MovieStatusSerializer
from api.serializers.social import SocialSerializer

class ProfileSerializer(serializers.ModelSerializer):
    animestatus = AnimeStatusSerializer(many=True)
    mangastatus = MangaStatusSerializer(many=True)
    moviestatus = MovieStatusSerializer(many=True)
    social = SocialSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'animestatus', 'mangastatus', 'moviestatus', 'social']
        depth = 3