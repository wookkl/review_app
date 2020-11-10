from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField
from . import choices


class User(AbstractUser):

    """ Custom User Model Definition """

    bio = models.TextField(null=True)
    preference = models.CharField(
        choices=choices.PREFERENCE_CHOICES, max_length=2, null=True, blank=True
    )
    language = models.CharField(
        choices=choices.LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    fav_books = MultiSelectField(
        choices=choices.BOOK_GENRE_CHOICES, null=True, blank=True
    )
    fav_movies = MultiSelectField(
        choices=choices.MOVIE_GENRE_CHOICES, null=True, blank=True
    )
