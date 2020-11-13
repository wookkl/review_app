from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel


class Category(TimeStampedModel):

    """ Category Model Definition """

    class Meta:
        verbose_name_plural = "categories"

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"
    KIND_CHOICES = (
        (KIND_BOOK, _("Book")),
        (KIND_MOVIE, _("Movie")),
        (KIND_BOTH, _("Both")),
    )
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=KIND_BOOK)

    def __str__(self):
        return self.name
