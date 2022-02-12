from django.urls import path

from api.views import manga

urlpatterns = [
    path('create', manga.create_manga),
    path('', manga.index_manga),
    path('<int:manga_id>', manga.get_manga),
    path('update/<int:manga_id>', manga.update_manga),
    path('delete/<int:manga_id>', manga.delete_manga),
]