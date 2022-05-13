from django.shortcuts import render
# Create your views here.
from api.models import Profile
from api.models import Manga
from api.models import Anime
from api.models import Movie
from api.models import Social
from api.models import AnimeStatus
from api.models import MangaStatus
from api.models import MovieStatus
from api.models import SeasonStatus
from api.models import Season
from api.models import Episode
from api.models import EpisodeStatus
from api.models import ChapterStatus
from api.models import Chapter
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

        # Adiciona animes ao perfil de usuário
        for anime in payload["animestatus"]:
            all_anime_status = AnimeStatus.objects.filter(profile=profile.id, anime=anime["id"])
            if (anime["delete"] and all_anime_status):
                all_anime_status.delete()
            elif (not anime["delete"] and not all_anime_status):
                all_anime_status = AnimeStatus.objects.create(
                    progress=0,
                    profile = profile,
                    anime=Anime.objects.get(id=anime["id"]),
                    favorite=anime["favorite"],
                )
            else: 
                all_anime_status.update(
                    favorite=anime["favorite"],
                )
            
            if (not anime["delete"]):
                for season in anime["seasonstatus"]:
                    all_anime_status = AnimeStatus.objects.get(profile=profile.id, anime=anime["id"])
                    all_season_status = SeasonStatus.objects.filter(animestatus=all_anime_status.id, season=season["id"])
                    if (not all_season_status):
                        all_season_status = SeasonStatus.objects.create(
                            progress=0,
                            animestatus=AnimeStatus.objects.get(id=all_anime_status.id),
                            season=Season.objects.get(id=season["id"]),
                        )
                    for episode in season["episodestatus"]:
                        all_season_status = SeasonStatus.objects.get(animestatus=all_anime_status.id, season=season["id"])
                        all_episode_status = EpisodeStatus.objects.filter(seasonstatus=all_season_status.id, episode=episode["id"])
                        if (not all_episode_status):
                            EpisodeStatus.objects.create(
                                progress=episode["progress"],
                                seasonstatus=SeasonStatus.objects.get(id=all_season_status.id),
                                episode=Episode.objects.get(id=episode["id"]),
                            )
                        else:
                            all_episode_status.update(
                                progress=episode["progress"],
                            )

        #Calcula progresso do anime e das temporadas
        for animestatus in AnimeStatus.objects.filter(profile=profile.id):
            progress_episode = 0
            qnt_episode = 0

            for seasonstatus in SeasonStatus.objects.filter(animestatus=animestatus.id):
                season_watched = True

                for episodestatus in EpisodeStatus.objects.filter(seasonstatus=seasonstatus.id):

                    if (episodestatus.progress != 100):
                        season_watched = False
                    progress_episode += episodestatus.progress
                    qnt_episode += 1

                # Se todos os episódios foram assistidos, marca a temporada como assistida
                if (season_watched):
                    SeasonStatus.objects.filter(animestatus=animestatus.id, season=seasonstatus.season.id).update(
                        progress= 100,
                    )
                else:
                     SeasonStatus.objects.filter(animestatus=animestatus.id, season=seasonstatus.season.id).update(
                         progress=0,
                    )

            # Calcula progresso do anime
            AnimeStatus.objects.filter(profile=profile.id, anime=animestatus.anime.id).update(
                progress=(progress_episode/qnt_episode),
            )


        # Adiciona filmes ao perfil de usuário
        for movie in payload["moviestatus"]:
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
                    favorite=movie["favorite"],
                    progress=movie["progress"],
                )

        # Adiciona mangas ao perfil de usuário
        for manga in payload["mangastatus"]:
            all_manga_status = MangaStatus.objects.filter(profile=profile.id, manga=manga["id"])
            if (manga["delete"] and all_manga_status):
                all_manga_status.delete()
            elif (not manga["delete"] and not all_manga_status):
                all_manga_status = MangaStatus.objects.create(
                    progress=0,
                    profile = profile,
                    manga=Manga.objects.get(id=manga["id"]),
                    favorite=manga["favorite"],
                )
            else:
                all_manga_status.update(
                    favorite=manga["favorite"],
                )

            if (not manga["delete"]):
                for chapter in manga["chapterstatus"]:
                    all_manga_status = MangaStatus.objects.get(profile=profile.id, manga=manga["id"])
                    all_chapter_status = ChapterStatus.objects.filter(mangastatus=all_manga_status.id, chapter=chapter["id"])
                    if (not all_chapter_status):
                        ChapterStatus.objects.create(
                            progress=chapter["progress"],
                            mangastatus=MangaStatus.objects.get(id=all_manga_status.id),
                            chapter=Chapter.objects.get(id=chapter["id"]),
                        )
                    else:
                        all_chapter_status.update(
                            progress=chapter["progress"],
                        )

        # Calcula o progresso do manga
        for mangastatus in MangaStatus.objects.filter(profile=profile.id):
            progress_chapter = 0
            qnt_chapter = 0

            for chapterstatus in ChapterStatus.objects.filter(mangastatus=mangastatus.id):
                progress_chapter += chapterstatus.progress
                qnt_chapter += 1

            MangaStatus.objects.filter(profile=profile.id, manga=mangastatus.manga.id).update(
                progress=(progress_chapter/qnt_chapter),
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