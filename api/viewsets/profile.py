from rest_framework import viewsets
from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()