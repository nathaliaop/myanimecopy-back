from django.urls import path

from api.views import anime

urlpatterns = [
    path('create', anime.create_anime),
    path('', anime.index_anime),
    path('<int:anime_id>', anime.get_anime),
    path('update/<int:anime_id>', anime.update_anime),
    path('delete/<int:anime_id>', anime.delete_anime),
]