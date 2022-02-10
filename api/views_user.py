from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
import json
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_user(request):
    users = User.objects
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_user(request):
    payload = json.loads(request.body)
    try:
        user = User.objects.create(
            username=payload["username"],
            email=payload["email"],
            password=payload["password"],
        )
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_user(request, user_id):
    payload = json.loads(request.body)
    try:
        user_item = User.objects.filter(id=user_id)
        user_item.update(**payload)
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)