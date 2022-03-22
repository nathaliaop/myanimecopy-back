from django.urls import path

from api.views import episode

urlpatterns = [
    path('create', episode.create_episode),
    path('', episode.index_episode),
    path('<int:episode_id>', episode.get_episode),
    path('update/<int:episode_id>', episode.update_episode),
    path('delete/<int:episode_id>', episode.delete_episode),
]