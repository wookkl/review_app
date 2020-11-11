from django.contrib.auth.models import AbstractUser
from django.db import models
from categories import models as category_models


class User(AbstractUser):

    """ Custom User Model Definition """

    LANG_ENGLISH = "en"
    LANG_KOREAN = "kr"
    LANG_JAPANESE = "jp"
    LANG_CHINESE = "cn"
    LANG_CHOICES = (
        (LANG_ENGLISH, "English"),
        (LANG_KOREAN, "Korean"),
        (LANG_JAPANESE, "Japanese"),
        (LANG_CHINESE, "Chinese"),
    )

    PREF_MOVIES = "mv"
    PREF_BOOKS = "bk"
    PREF_CHOICES = (
        (PREF_MOVIES, "Movies"),
        (PREF_BOOKS, "Books"),
    )

    bio = models.TextField(blank=True)
    preference = models.CharField(
        choices=PREF_CHOICES, max_length=2, default=PREF_BOOKS
    )
    language = models.CharField(
        choices=LANG_CHOICES, max_length=2, default=LANG_ENGLISH
    )
    fav_book_genre = models.ForeignKey(
        category_models.Category,
        null=True,
        on_delete=models.PROTECT,
        related_name="users_fav_book",
    )
    fav_movie_genre = models.ForeignKey(
        category_models.Category,
        null=True,
        on_delete=models.PROTECT,
        related_name="users_fav_movie",
    )
