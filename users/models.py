from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from . import choices


class User(AbstractUser):

    """ Custom User Model Definition """

    bio = models.TextField(blank=True)
    preference = models.CharField(
        choices=choices.PREFERENCE_CHOICES, max_length=2, blank=True
    )
    language = models.CharField(
        choices=choices.LANGUAGE_CHOICES, max_length=2, blank=True
    )
    favorite_book_genres = MultiSelectField(
        choices=choices.BOOK_GENRE_CHOICES, null=True, blank=True
    )
    favorite_movie_genres = MultiSelectField(
        choices=choices.MOVIE_GENRE_CHOICES, null=True, blank=True
    )
