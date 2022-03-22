from django.urls import path

from api.views import genre

urlpatterns = [
    path('create', genre.create_genre),
    path('', genre.index_genre),
    path('<int:genre_id>', genre.get_genre),
    path('update/<int:genre_id>', genre.update_genre),
    path('delete/<int:genre_id>', genre.delete_genre),
]