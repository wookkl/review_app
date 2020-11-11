from django.db import models
from core.models import TimeStampedModel


class Person(TimeStampedModel):

    """ Person Model Definition """

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_ACTOR)
    photo = models.ImageField(null=True, blank=True)
