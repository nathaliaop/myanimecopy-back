from django.urls import path
from . import views_anime

urlpatterns = [
    path('animes/create', views_anime.create_anime),
    path('animes/update', views_anime.update_anime),
    path('animes', views_anime.index_anime),
    path('animes/<int:anime_id>', views_anime.get_anime),
    path('animes/update/<int:anime_id>', views_anime.update_anime),
    path('animes/delete/<int:anime_id>', views_anime.delete_anime),
]