from rest_framework import serializers
from api.models.season import Season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'anime', 'number']
        depth = 1