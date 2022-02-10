from django.shortcuts import render

# Create your views here.
from .models import Genre
import json
from .serializers import GenreSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_genre(request, genre_id):
    #user = request.user.id
    genre = Genre.objects.get(id=genre_id)
    serializer = GenreSerializer(genre)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_genre(request):
    #user = request.user.id
    genres = Genre.objects#.filter(added_by=user)
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_genre(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        genre = Genre.objects.create(
            name=payload["name"],
            #added_by=user,
        )
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_genre(request, genre_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        genre_item = Genre.objects.filter(id=genre_id)
        # returns 1 or 0
        genre_item.update(**payload)
        genre = Genre.objects.get(id=genre_id)
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_genre(request, genre_id):
    #user = request.user.id
    try:
        genre = Genre.objects.get(id=genre_id)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)