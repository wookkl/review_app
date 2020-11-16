from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel


class Person(TimeStampedModel):

    """ Person Model Definition """

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, _("Actor")),
        (KIND_DIRECTOR, _("Director")),
        (KIND_WRITER, _("Writer")),
    )

    name = models.CharField(max_length=120)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    photo = models.ImageField(null=True, blank=True, upload_to="person_photos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "people"
