from django.urls import path

from .views import anime, chapter, episode, genre, manga, movie, profile, season

urlpatterns = [

    path('movies/create', movie.create_movie),
    path('movies/update', movie.update_movie),
    path('movies', movie.index_movie),
    path('movies/<int:movie_id>', movie.get_movie),
    path('movies/update/<int:movie_id>', movie.update_movie),
    path('movies/delete/<int:movie_id>', movie.delete_movie),

    path('animes/create', anime.create_anime),
    path('animes/update', anime.update_anime),
    path('animes', anime.index_anime),
    path('animes/<int:anime_id>', anime.get_anime),
    path('animes/update/<int:anime_id>', anime.update_anime),
    path('animes/delete/<int:anime_id>', anime.delete_anime),

    path('mangas/create', manga.create_manga),
    path('mangas/update', manga.update_manga),
    path('mangas', manga.index_manga),
    path('mangas/<int:manga_id>', manga.get_manga),
    path('mangas/update/<int:manga_id>', manga.update_manga),
    path('mangas/delete/<int:manga_id>', manga.delete_manga),

    path('genres/create', genre.create_genre),
    path('genres/update', genre.update_genre),
    path('genres', genre.index_genre),
    path('genres/<int:genre_id>', genre.get_genre),
    path('genres/update/<int:genre_id>', genre.update_genre),
    path('genres/delete/<int:genre_id>', genre.delete_genre),

    path('chapters/create', chapter.create_chapter),
    path('chapters/update', chapter.update_chapter),
    path('chapters', chapter.index_chapter),
    path('chapters/<int:chapter_id>', chapter.get_chapter),
    path('chapters/update/<int:chapter_id>', chapter.update_chapter),
    path('chapters/delete/<int:chapter_id>', chapter.delete_chapter),

    path('seasons/create', season.create_season),
    path('seasons/update', season.update_season),
    path('seasons', season.index_season),
    path('seasons/<int:season_id>', season.get_season),
    path('seasons/update/<int:season_id>', season.update_season),
    path('seasons/delete/<int:season_id>', season.delete_season),

    path('episodes/create', episode.create_episode),
    path('episodes/update', episode.update_episode),
    path('episodes', episode.index_episode),
    path('episodes/<int:episode_id>', episode.get_episode),
    path('episodes/update/<int:episode_id>', episode.update_episode),
    path('episodes/delete/<int:episode_id>', episode.delete_episode),

    path('profiles/create', profile.create_profile),
    path('profiles/update', profile.update_profile),
    path('profiles', profile.index_profile),
    path('profiles/<int:profile_id>', profile.get_profile),
    path('profiles/update/<int:profile_id>', profile.update_profile),
    path('profiles/delete/<int:profile_id>', profile.delete_profile),
]