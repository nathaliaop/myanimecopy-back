from django.shortcuts import render

# Create your views here.
from .models import Tag, Chapter
import json
from .serializers import ChapterSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_chapter(request, chapter_id):
    #user = request.user.id
    chapter = Chapter.objects.get(id=chapter_id)
    serializer = ChapterSerializer(chapter)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_chapter(request):
    #user = request.user.id
    chapters = Chapter.objects#.filter(added_by=user)
    serializer = ChapterSerializer(chapters, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_chapter(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        tag = Tag.objects.get(id=payload["tag"])
        chapter = Chapter.objects.create(
            title=payload["title"],
            description=payload["description"],
            release_date=payload["release_date"],
            image=payload["image"],
            tag=tag,
            #added_by=user,
        )
        serializer = ChapterSerializer(chapter)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_chapter(request, chapter_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        chapter_item = Chapter.objects.filter(id=chapter_id)
        # returns 1 or 0
        chapter_item.update(**payload)
        chapter = Chapter.objects.get(id=chapter_id)
        serializer = ChapterSerializer(chapter)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_chapter(request, chapter_id):
    #user = request.user.id
    try:
        chapter = Chapter.objects.get(id=chapter_id)
        chapter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)