from django.urls import path

from api.views import chapter

urlpatterns = [
    path('create', chapter.create_chapter),
    path('', chapter.index_chapter),
    path('<int:chapter_id>', chapter.get_chapter),
    path('update/<int:chapter_id>', chapter.update_chapter),
    path('delete/<int:chapter_id>', chapter.delete_chapter),
]