from django.shortcuts import render

# Create your views here.
from .models import Social, Profile
import json
from .serializers import SocialSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_social(request, social_id):
    social = Social.objects.get(id=social_id)
    serializer = SocialSerializer(social)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_social(request):
    socials = Social.objects#.filter(added_by=user)
    serializer = SocialSerializer(socials, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_social(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        profile = Profile.objects.get(id=payload["profile"])
        social = Social.objects.create(
            profile=profile,
            #added_by=user,
        )

        for i in payload["following"]:
            social.following.add(i)
            other_user_profile = Profile.objects.get(id=i)
            other_user_profile.social.followers.add(profile.id)

        serializer = SocialSerializer(social)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_social(request, social_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        social_item = Social.objects.filter(id=social_id)
        # returns 1 or 0
        social_item.update(**payload)
        social = Social.objects.get(id=social_id)
        serializer = SocialSerializer(social)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_social(request, social_id):
    #user = request.user.id
    try:
        social = Social.objects.get(id=social_id)
        social.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)