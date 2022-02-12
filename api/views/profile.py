from django.shortcuts import render
# Create your views here.
from api.models.profile import Profile
from api.models.manga import Manga
from api.models.anime import Anime
from api.models.movie import Movie
from api.models.social import Social
from django.contrib.auth.models import User
from api.serializers.profile import ProfileSerializer
import json
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(["GET"])
def get_profile(request, profile_id):
    #user = request.user.id
    profile = Profile.objects.get(id=profile_id)
    serializer = ProfileSerializer(profile)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def index_profile(request):
    #user = request.user.id
    profiles = Profile.objects#.filter(added_by=user)
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_profile(request):
    # user = request.user
    payload = json.loads(request.body)
    try:

        user = User.objects.create(
            username=payload["username"],
            password=payload["password"],
            email=payload["email"],
            #added_by=user,
        )

        profile = Profile.objects.create(
            user=user,
            image=payload["image"],
            #added_by=user,
        )

        Social.objects.create(
            profile=profile,
        )

        '''for manga in payload["mangas"]:
            profile.mangas.add(manga["id"])
            add_manga = Manga.objects.filter(id=manga["id"])
            add_manga.update(tag=manga["tag"])
            
        for anime in payload["animes"]:
            profile.animes.add(anime["id"])
            add_anime = Anime.objects.filter(id=anime["id"])
            add_anime.update(tag=anime["tag"])

        for movie in payload["movies"]:
            profile.movies.add(movie["id"])
            add_movie = Movie.objects.filter(id=movie["id"])
            add_movie.update(tag=movie["tag"])'''

        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo deu errado'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
def update_profile(request, profile_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        profile = Profile.objects.filter(id=profile_id)
        # returns 1 or 0
        user = User.objects.filter(id=profile_id)

        profile.update(
            image=payload["image"],
        )

        user.update(
            email=payload["email"],
            username=payload["username"],
            password=payload["password"],
        )

        '''for profile in Profile.objects.filter(id=profile_id):
            for anime in payload["animes"]:
                if (anime["delete"]):
                    profile.animes.remove(anime["id"])
                else:
                    profile.animes.add(anime["id"])
                    add_anime = Anime.objects.filter(id=anime["id"])
                    #add_anime.update(tag=anime["tag"])

            
            for movie in payload["movies"]:
                if (movie["delete"]):
                    profile.movies.remove(movie["id"])
                else:
                    profile.movies.add(movie["id"])
                    add_movie = Movie.objects.filter(id=movie["id"])
                    add_movie.update(tag=movie["tag"])

            for manga in payload["mangas"]:
                if (manga["delete"]):
                    profile.mangas.remove(manga["id"])
                else:
                    profile.mangas.add(manga["id"])
                    add_manga = Manga.objects.filter(id=manga["id"])
                    add_manga.update(tag=manga["tag"])'''

        for social in Social.objects.filter(id=profile_id):
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