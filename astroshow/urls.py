from django.urls import path, include
from rest_framework.routers import DefaultRouter

from astroshow.views import ReservationViewSet, ShowThemeViewSet, AstronomyShowViewSet, PlanetariumDomeViewSet, \
    ShowSessionViewSet, TicketViewSet

router = DefaultRouter()
router.register("shows", AstronomyShowViewSet)
router.register("themes", ShowThemeViewSet)
router.register("domes", PlanetariumDomeViewSet)
router.register("sessions", ShowSessionViewSet)
router.register("tickets", TicketViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

