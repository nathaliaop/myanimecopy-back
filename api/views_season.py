from django.shortcuts import render

# Create your views here.
from .models import Season, Anime
import json
from .serializers import SeasonSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_season(request, season_id):
    #user = request.user.id
    season = Season.objects.get(id=season_id)
    serializer = SeasonSerializer(season)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_season(request):
    #user = request.user.id
    seasons = Season.objects#.filter(added_by=user)
    serializer = SeasonSerializer(seasons, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_season(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        anime = Anime.objects.get(id=payload["anime"])
        season = Season.objects.create(
            number=payload["number"],
            anime=anime,
            #added_by=user,
        )
        serializer = SeasonSerializer(season)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_season(request, season_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        season_item = Season.objects.filter(id=season_id)
        # returns 1 or 0
        season_item.update(**payload)
        season = Season.objects.get(id=season_id)
        serializer = SeasonSerializer(season)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_season(request, season_id):
    #user = request.user.id
    try:
        season = Season.objects.get(id=season_id)
        season.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)