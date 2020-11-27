from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class User(AbstractUser):

    """ Custom User Model Definition """

    LANG_ENGLISH = "en"
    LANG_KOREAN = "kr"
    LANG_JAPANESE = "jp"
    LANG_CHINESE = "cn"
    LANG_CHOICES = (
        (LANG_ENGLISH, _("English")),
        (LANG_KOREAN, _("Korean")),
        (LANG_JAPANESE, _("Japanese")),
        (LANG_CHINESE, _("Chinese")),
    )

    PREF_MOVIES = "mv"
    PREF_BOOKS = "bk"
    PREF_CHOICES = (
        (PREF_MOVIES, _("Movies")),
        (PREF_BOOKS, _("Books")),
    )

    bio = models.TextField(blank=True)
    preference = models.CharField(
        choices=PREF_CHOICES, max_length=2, default=PREF_BOOKS
    )
    language = models.CharField(
        choices=LANG_CHOICES, max_length=2, default=LANG_ENGLISH
    )
    fav_book_genre = models.ForeignKey(
        "categories.Category",
        null=True,
        on_delete=models.SET_NULL,
        related_name="users_fav_book",
    )
    fav_movie_genre = models.ForeignKey(
        "categories.Category",
        null=True,
        on_delete=models.SET_NULL,
        related_name="users_fav_movie",
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
