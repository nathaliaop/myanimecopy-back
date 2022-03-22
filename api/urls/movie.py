from django.urls import path

from api.views import movie

urlpatterns = [
    path('create', movie.create_movie),
    path('', movie.index_movie),
    path('<int:movie_id>', movie.get_movie),
    path('update/<int:movie_id>', movie.update_movie),
    path('delete/<int:movie_id>', movie.delete_movie),
]