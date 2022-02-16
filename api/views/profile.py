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
from api.models.seasonstatus import SeasonStatus
from api.models.season import Season
from api.models.episode import Episode
from api.models.episodestatus import EpisodeStatus
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
        Profile.objects.filter(id=profile_id).update(
            image=payload["image"],
        )
        User.objects.filter(id=profile_id).update(
            email=payload["email"],
            username=payload["username"],
            password=payload["password"],
        )

        profile = Profile.objects.get(id=profile_id)
        social = Social.objects.get(id=profile_id)
        for anime in payload["animes"]:
            all_anime_status = AnimeStatus.objects.filter(profile=profile.id, anime=anime["id"])
            if (anime["delete"] and all_anime_status):
                all_anime_status.delete()
            elif (not anime["delete"] and not all_anime_status):
                all_anime_status = AnimeStatus.objects.create(
                    profile = profile,
                    anime=Anime.objects.get(id=anime["id"]),
                    favorite=anime["favorite"],
                    progress=anime["progress"],
                )
            else: 
                all_anime_status.update(
                    profile = profile,
                    anime=anime["id"],
                    favorite=anime["favorite"],
                    progress=anime["progress"],
                )
            for season in anime["seasons"]:
                all_anime_status = AnimeStatus.objects.get(profile=profile.id, anime=anime["id"])
                all_season_status = SeasonStatus.objects.filter(animestatus=all_anime_status.id, season=season["id"])
                if (not all_season_status):
                    all_season_status = SeasonStatus.objects.create(
                        progress=season["progress"],
                        animestatus=AnimeStatus.objects.get(id=all_anime_status.id),
                        season=Season.objects.get(id=season["id"]),
                    )
                else:
                    all_season_status.update(
                        progress=season["progress"],
                        animestatus=AnimeStatus.objects.get(id=all_anime_status.id),
                        season=Season.objects.get(id=all_season_status[0].id),
                    )
                for episode in season["episodes"]:
                    all_season_status = SeasonStatus.objects.get(animestatus=all_anime_status.id, season=season["id"])
                    all_episode_status = EpisodeStatus.objects.filter(seasonstatus=all_season_status.id, episode=episode["id"])
                    if (not all_episode_status):
                        EpisodeStatus.objects.create(
                            progress=episode["progress"],
                            seasonstatus=SeasonStatus.objects.get(id=all_season_status.id),
                            episode=Episode.objects.get(id=episode["id"]),
                        )
                    else:
                        EpisodeStatus.objects.update(
                            progress=episode["progress"],
                            seasonstatus=SeasonStatus.objects.get(id=all_season_status.id),
                            episode=Episode.objects.get(id=all_episode_status[0].id),
                        )


        for movie in payload["movies"]:
            all_movie_status = MovieStatus.objects.filter(profile=profile.id, movie=movie["id"])
            if (movie["delete"] and all_movie_status):
                all_movie_status.delete()
            elif (not movie["delete"] and not all_movie_status):
                MovieStatus.objects.create(
                    profile = profile,
                    movie=Movie.objects.get(id=movie["id"]),
                    favorite=movie["favorite"],
                    progress=movie["progress"],
                )
            else:
                all_movie_status.update(
                    profile = profile,
                    movie=movie["id"],
                    favorite=movie["favorite"],
                    progress=movie["progress"],
                )

        for manga in payload["mangas"]:
            all_manga_status = MangaStatus.objects.filter(profile=profile.id, manga=manga["id"])
            if (manga["delete"] and all_manga_status):
                all_manga_status.delete()
            elif (not manga["delete"] and not all_manga_status):
                mangastatus = MangaStatus.objects.create(
                    profile = profile,
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
            else:
                all_manga_status.update(
                    profile = profile,
                    manga=manga["id"],
                    favorite=manga["favorite"],
                    progress=manga["progress"],
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