from .anime import Anime
from .chapter import Chapter
from .episode import Episode
from .genre import Genre
from .manga import Manga
from .movie import Movie
from .profile import Profile
from .season import Season
from .social import Social
from .animestatus import AnimeStatus
from .mangastatus import MangaStatus
from .moviestatus import MovieStatus
from .chapterstatus import ChapterStatus
from .seasonstatus import SeasonStatus
from .episodestatus import EpisodeStatus

genre_list= ["adventure", "action", "drama", "mecha"]

for title in genre_list:
    Genre.objects.get_or_create(
        title=title
    )