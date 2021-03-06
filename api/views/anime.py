from django.shortcuts import render

# Create your views here.
from api.models import Anime
from api.models import Season
from api.models import Episode
from api.serializers.anime import AnimeSerializer
import json
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_anime(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    serializer = AnimeSerializer(anime)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_anime(request):
    animes = Anime.objects#.filter(added_by=user)
    serializer = AnimeSerializer(animes, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_anime(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        anime = Anime.objects.create(
            studio=payload["studio"],
            director=payload["director"],
            title=payload["title"],
            description=payload["description"],
            release_date=payload["release_date"],
            image=payload["image"],
            #added_by=user,
        )

        for season in payload["seasons"]:
            add_season = Season.objects.create(
                anime=anime,
                number=season["number"],
            )
            for episode in season["episodes"]:
                Episode.objects.create(
                    season=add_season,
                    title=episode["title"],
                    number=episode["number"],
                )

        for genre in payload["genres"]:
            anime.genres.add(genre)

        serializer = AnimeSerializer(anime)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_anime(request, anime_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        anime_item = Anime.objects.filter(id=anime_id)
        # returns 1 or 0
        anime_item.update(**payload)
        anime = Anime.objects.get(id=anime_id)
        serializer = AnimeSerializer(anime)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_anime(request, anime_id):
    #user = request.user.id
    try:
        anime = Anime.objects.get(id=anime_id)
        anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)