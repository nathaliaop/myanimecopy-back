from django.shortcuts import render

# Create your views here.
from api.models.chapter import Chapter
from api.models.manga import Manga
from api.serializers.manga import MangaSerializer
import json
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_manga(request, manga_id):
    #user = request.user.id
    manga = Manga.objects.get(id=manga_id)
    serializer = MangaSerializer(manga)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_manga(request):
    #user = request.user.id
    mangas = Manga.objects#.filter(added_by=user)
    serializer = MangaSerializer(mangas, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_manga(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        manga = Manga.objects.create(
            author=payload["author"],
            title=payload["title"],
            description=payload["description"],
            release_date=payload["release_date"],
            image=payload["image"],
            #added_by=user,
        )

        for chapter in payload["chapters"]:
            Chapter.objects.create(
                manga=manga,
                number=chapter["number"],
                name=chapter["name"],
            )


        for genre in payload["genres"]:
            manga.genres.add(genre)

        serializer = MangaSerializer(manga)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_manga(request, manga_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        manga_item = Manga.objects.filter(id=manga_id)
        # returns 1 or 0
        manga_item.update(**payload)
        manga = Manga.objects.get(id=manga_id)
        serializer = MangaSerializer(manga)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_manga(request, manga_id):
    #user = request.user.id
    try:
        manga = Manga.objects.get(id=manga_id)
        manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)