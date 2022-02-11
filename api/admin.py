from django.contrib import admin
from .models import Genre, Movie, Anime, Manga, Season, Episode, Chapter, Profile

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Chapter)
admin.site.register(Profile)