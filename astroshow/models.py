from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, User


class AstronomyShow(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    themes = models.ManyToManyField("ShowTheme", related_name="shows")

    def __str__(self):
        return self.title


class ShowTheme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PlanetariumDome(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seat_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation #{self.id} by {self.user.username}"

    class Meta:
        ordering = ["-created_at"]

class ShowSession(models.Model):
    id = models.AutoField(primary_key=True)
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return self.astronomy_show.title


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.row}-{self.seat} for {self.show_session}"

    class Meta:
        unique_together = ("show_session", "row", "seat")

