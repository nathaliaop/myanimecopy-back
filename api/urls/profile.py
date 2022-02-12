from django.urls import path

from api.views import profile

urlpatterns = [
    path('create', profile.create_profile),
    path('', profile.index_profile),
    path('<int:profile_id>', profile.get_profile),
    path('update/<int:profile_id>', profile.update_profile),
    path('delete/<int:profile_id>', profile.delete_profile),
]