# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# local Django
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin Definition """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "language",
                    "preference",
                    "fav_book_genre",
                    "fav_movie_genre",
                    "login_method",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
        "login_method",

    )

    list_filter = (
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )
