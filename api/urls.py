from django.urls import path
from . import views_tag, views_movie, views_anime, views_manga, views_genre, views_season, views_episode, views_chapter

urlpatterns = [
    path('tags/create', views_tag.create_tag),
    path('tags/update', views_tag.update_tag),
    path('tags', views_tag.index_tag),
    path('tags/<int:tag_id>', views_tag.get_tag),
    path('tags/update/<int:tag_id>', views_tag.update_tag),
    path('tags/delete/<int:tag_id>', views_tag.delete_tag),

    path('movies/create', views_movie.create_movie),
    path('movies/update', views_movie.update_movie),
    path('movies', views_movie.index_movie),
    path('movies/<int:movie_id>', views_movie.get_movie),
    path('movies/update/<int:movie_id>', views_movie.update_movie),
    path('movies/delete/<int:movie_id>', views_movie.delete_movie),

    path('animes/create', views_anime.create_anime),
    path('animes/update', views_anime.update_anime),
    path('animes', views_anime.index_anime),
    path('animes/<int:anime_id>', views_anime.get_anime),
    path('animes/update/<int:anime_id>', views_anime.update_anime),
    path('animes/delete/<int:anime_id>', views_anime.delete_anime),

    path('mangas/create', views_manga.create_manga),
    path('mangas/update', views_manga.update_manga),
    path('mangas', views_manga.index_manga),
    path('mangas/<int:manga_id>', views_manga.get_manga),
    path('mangas/update/<int:manga_id>', views_manga.update_manga),
    path('mangas/delete/<int:manga_id>', views_manga.delete_manga),

    path('genres/create', views_genre.create_genre),
    path('genres/update', views_genre.update_genre),
    path('genres', views_genre.index_genre),
    path('genres/<int:genre_id>', views_genre.get_genre),
    path('genres/update/<int:genre_id>', views_genre.update_genre),
    path('genres/delete/<int:genre_id>', views_genre.delete_genre),

    path('seasons/create', views_season.create_season),
    path('seasons/update', views_season.update_season),
    path('seasons', views_season.index_season),
    path('seasons/<int:season_id>', views_season.get_season),
    path('seasons/update/<int:season_id>', views_season.update_season),
    path('seasons/delete/<int:season_id>', views_season.delete_season),

    path('episodes/create', views_episode.create_episode),
    path('episodes/update', views_episode.update_episode),
    path('episodes', views_episode.index_episode),
    path('episodes/<int:episode_id>', views_episode.get_episode),
    path('episodes/update/<int:episode_id>', views_episode.update_episode),
    path('episodes/delete/<int:episode_id>', views_episode.delete_episode),

    path('chapters/create', views_chapter.create_chapter),
    path('chapters/update', views_chapter.update_chapter),
    path('chapters', views_chapter.index_chapter),
    path('chapters/<int:chapter_id>', views_chapter.get_chapter),
    path('chapters/update/<int:chapter_id>', views_chapter.update_chapter),
    path('chapters/delete/<int:chapter_id>', views_chapter.delete_chapter),
]