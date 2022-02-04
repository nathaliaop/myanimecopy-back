from django.urls import path
from . import views

urlpatterns = [
    path('animes/create', views.create_anime),
    path('animes/update', views.update_anime),
    path('animes', views.index_anime),
    path('animes/<int:anime_id>', views.get_anime),
    path('animes/update/<int:anime_id>', views.update_anime),
    path('animes/delete/<int:anime_id>', views.delete_anime),
    path('tags', views.tags, name='tags'),
    path('movies', views.movies, name='movies'),
    path('mangas', views.mangas, name='mangas'),
]