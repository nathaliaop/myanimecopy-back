from django.shortcuts import render

# Create your views here.
from .models import Favorite, Profile
import json
from .serializers import FavoriteSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_favorite(request, favorite_id):
    #user = request.user.id
    favorite = Favorite.objects.get(id=favorite_id)
    serializer = FavoriteSerializer(favorite)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_favorite(request):
    #user = request.user.id
    favorites = Favorite.objects#.filter(added_by=user)
    serializer = FavoriteSerializer(favorites, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_favorite(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        profile = Profile.objects.get(id=payload["profile"])
        favorite = Favorite.objects.create(
            profile=profile,
            #added_by=user,
        )

        for i in payload["animes"]:
            favorite.animes.add(i)

        for i in payload["movies"]:
            favorite.movies.add(i)

        for i in payload["mangas"]:
            favorite.mangas.add(i)

        serializer = FavoriteSerializer(favorite)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_favorite(request, favorite_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        favorite_item = Favorite.objects.filter(id=favorite_id)
        # returns 1 or 0
        favorite_item.update(**payload)
        favorite = Favorite.objects.get(id=favorite_id)
        serializer = FavoriteSerializer(favorite)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_favorite(request, favorite_id):
    #user = request.user.id
    try:
        favorite = Favorite.objects.get(id=favorite_id)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)