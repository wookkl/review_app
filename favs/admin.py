from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavAdmin(admin.ModelAdmin):

    """ Fav Admin Definition """

    list_display = ("__str__",)

    list_filter = (
        "books",
        "movies",
    )
