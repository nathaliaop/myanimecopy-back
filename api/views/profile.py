from django.shortcuts import render
# Create your views here.
from api.models.profile import Profile
from api.models.manga import Manga
from api.models.anime import Anime
from api.models.movie import Movie
from api.models.social import Social
from api.models.animestatus import AnimeStatus
from api.models.mangastatus import MangaStatus
from api.models.moviestatus import MovieStatus
from api.models.chapterstatus import ChapterStatus
from api.models.chapter import Chapter
from django.contrib.auth.models import User
from api.serializers.profile import ProfileSerializer
import json
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response


from asgiref.sync import sync_to_async

@api_view(["GET"])
def get_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    serializer = ProfileSerializer(profile)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_profile(request):
    profiles = Profile.objects
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_profile(request):
    payload = json.loads(request.body)
    try:

        user = User.objects.create(
            username=payload["username"],
            password=payload["password"],
            email=payload["email"],
        )

        profile = Profile.objects.create(
            user=user,
            image=payload["image"],
        )

        Social.objects.create(
            profile=profile,
        )

        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_profile(request, profile_id):
    payload = json.loads(request.body)
    try:
        profile = Profile.objects.filter(id=profile_id)
        social = Social.objects.get(id=profile_id)
        user = User.objects.filter(id=profile_id)

        profile.update(
            image=payload["image"],
        )

        user.update(
            email=payload["email"],
            username=payload["username"],
            password=payload["password"],
        )

        for anime in payload["animes"]:
            if (anime["delete"]):
                for remove_status in AnimeStatus.objects.filter(profile=profile.id, anime=anime["id"]):
                    remove_status.delete()
            else:
                AnimeStatus.objects.create(
                    profile = Profile.objects.get(id=profile_id),
                    anime=Anime.objects.get(id=anime["id"]),
                    favorite=anime["favorite"],
                    progress=anime["progress"],
                )
        for movie in payload["movies"]:
            if (movie["delete"]):
                for remove_status in MovieStatus.objects.filter(profile=profile.id, movie=movie["id"]):
                    remove_status.delete()
            else:
                MovieStatus.objects.create(
                    profile = Profile.objects.get(id=profile_id),
                    movie=Movie.objects.get(id=movie["id"]),
                    favorite=movie["favorite"],
                    progress=movie["progress"],
                )
        for manga in payload["mangas"]:
            if (manga["delete"]):
                for remove_status in MangaStatus.objects.filter(profile=profile.id, manga=manga["id"]):
                    remove_status.delete()
            else:
                mangastatus = MangaStatus.objects.create(
                    profile = Profile.objects.get(id=profile_id),
                    manga=Manga.objects.get(id=manga["id"]),
                    favorite=manga["favorite"],
                    progress=manga["progress"],
                )

            for chapter in manga["chapters"]:  
                ChapterStatus.objects.create(
                    mangastatus=MangaStatus.objects.get(id=mangastatus.id),
                    chapter=Chapter.objects.get(id=chapter["id"]),
                    progress=chapter["progress"],
                )

        for follower in payload["followers"]:
            if (follower["delete"]):
                social.following.remove(follower["id"])
                for remove_follower in Social.objects.filter(id=follower["id"]):
                    remove_follower.followers.remove(social.id)
            else:
                social.following.add(follower["id"])
                for add_follower in Social.objects.filter(id=follower["id"]):
                    add_follower.followers.add(social.id)

        profile = Profile.objects.get(id=profile_id)
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_profile(request, profile_id):
    #user = request.user.id
    try:
        profile = Profile.objects.get(id=profile_id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)