from rest_framework import serializers
from api.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'animes', 'movies', 'mangas', 'favorite', 'social']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value