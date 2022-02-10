from django.shortcuts import render

# Create your views here.
from .models import Episode, Season
import json
from .serializers import EpisodeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_episode(request, episode_id):
    #user = request.user.id
    episode = Episode.objects.get(id=episode_id)
    serializer = EpisodeSerializer(episode)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_episode(request):
    #user = request.user.id
    episodes = Episode.objects#.filter(added_by=user)
    serializer = EpisodeSerializer(episodes, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_episode(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        season = Season.objects.get(id=payload["season"])
        episode = Episode.objects.create(
            number=payload["number"],
            season=season,
            #added_by=user,
        )
        serializer = EpisodeSerializer(episode)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_episode(request, episode_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        episode_item = Episode.objects.filter(id=episode_id)
        # returns 1 or 0
        episode_item.update(**payload)
        episode = Episode.objects.get(id=episode_id)
        serializer = EpisodeSerializer(episode)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_episode(request, episode_id):
    #user = request.user.id
    try:
        episode = Episode.objects.get(id=episode_id)
        episode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)