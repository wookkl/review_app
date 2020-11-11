from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from . import choices


class User(AbstractUser):

    """ Custom User Model Definition """

    bio = models.TextField(blank=True)
    preference = models.CharField(
        choices=choices.PREF_CHOICES, max_length=2, default=choices.PREF_BOOKS
    )
    language = models.CharField(
        choices=choices.LANG_CHOICES, max_length=2, default=choices.LANG_ENGLISH
    )
    fav_book_genres = MultiSelectField(choices=choices.GENRE_CHOICES, null=True)
    fav_movie_genres = MultiSelectField(choices=choices.GENRE_CHOICES, null=True)
