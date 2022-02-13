from rest_framework import serializers
from api.models.animestatus import AnimeStatus

class AnimeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeStatus
        fields = ['id', 'favorite', 'progress', 'anime']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value