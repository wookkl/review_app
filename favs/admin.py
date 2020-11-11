from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavAdmin(admin.ModelAdmin):

    """ Fav Admin Definition """

    list_display = ("created_by",)

    list_filter = (
        "created_by",
        "books",
        "movies",
    )
