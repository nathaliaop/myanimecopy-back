from django.shortcuts import render

# Create your views here.
from ..models import Movie, Tag
import json
from ..serializers import MovieSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_movie(request, movie_id):
    #user = request.user.id
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_movie(request):
    #user = request.user.id
    movies = Movie.objects#.filter(added_by=user)
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_movie(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        tag = Tag.objects.get(id=payload["tag"])
        movie = Movie.objects.create(
            tag=tag,
            studio=payload["studio"],
            director=payload["director"],
            title=payload["title"],
            description=payload["description"],
            release_date=payload["release_date"],
            image=payload["image"],
            #added_by=user,
        )

        for i in payload["genres"]:
            movie.genres.add(i)

        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_movie(request, movie_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        movie_item = Movie.objects.filter(id=movie_id)
        # returns 1 or 0
        movie_item.update(**payload)
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_movie(request, movie_id):
    #user = request.user.id
    try:
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)