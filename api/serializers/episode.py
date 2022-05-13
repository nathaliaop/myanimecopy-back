from rest_framework import serializers
from api.models import Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'number']
        depth = 2
