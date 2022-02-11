from django.shortcuts import render

# Create your views here.
from ..models import Tag
import json
from ..serializers import TagSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_tag(request, tag_id):
    #user = request.user.id
    tag = Tag.objects.get(id=tag_id)
    serializer = TagSerializer(tag)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_tag(request):
    #user = request.user.id
    tags = Tag.objects#.filter(added_by=user)
    serializer = TagSerializer(tags, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_tag(request):
    # user = request.user
    payload = json.loads(request.body)
    try:
        tag = Tag.objects.create(
            name=payload["name"],
            #added_by=user,
        )
        serializer = TagSerializer(tag)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_tag(request, tag_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        tag_item = Tag.objects.filter(id=tag_id)
        # returns 1 or 0
        tag_item.update(**payload)
        tag = Tag.objects.get(id=tag_id)
        serializer = TagSerializer(tag)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_tag(request, tag_id):
    #user = request.user.id
    try:
        tag = Tag.objects.get(id=tag_id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)