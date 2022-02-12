from django.urls import path

from api.views import season

urlpatterns = [
    path('create', season.create_season),
    path('', season.index_season),
    path('<int:season_id>', season.get_season),
    path('update/<int:season_id>', season.update_season),
    path('delete/<int:season_id>', season.delete_season),
]