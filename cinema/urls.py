from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
