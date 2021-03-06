# Django
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# local Django
from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model Definition """

    LOGIN_GITHUB = "GH"
    LOGIN_KAKAO = "KK"
    LOGIN_EMAIL = "EM"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, _("Email")),
        (LOGIN_GITHUB, _("Github")),
        (LOGIN_KAKAO, _("Kakao")),
    )

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
    login_method = models.CharField(choices=LOGIN_CHOICES, max_length=2, default=LOGIN_EMAIL)
    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
