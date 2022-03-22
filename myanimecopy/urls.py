from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('api.urls.movie')),
    path('animes/', include('api.urls.anime')),
    path('mangas/', include('api.urls.manga')),
    path('genres/', include('api.urls.genre')),
    path('chapters/', include('api.urls.chapter')),
    path('seasons/', include('api.urls.season')),
    path('episodes/', include('api.urls.episode')),
    path('profiles/', include('api.urls.profile')),
]