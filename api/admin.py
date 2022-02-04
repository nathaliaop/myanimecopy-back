from django.contrib import admin
from .models import Tag, Movie, Anime, Manga

# Register your models here.
admin.site.register(Tag)
admin.site.register(Movie)
admin.site.register(Anime)
admin.site.register(Manga)