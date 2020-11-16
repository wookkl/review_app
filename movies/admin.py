from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """ Movie Admin Definition """

    list_display = (
        "title",
        "get_thumbnail",
        "year",
        "director",
        "rating",
    )

    list_filter = ("category", "director", "cast")

    def get_thumbnail(self, obj):
        print(obj.cover_image.url)
        return mark_safe(
            f'<a href="{obj.cover_image.url}"><img src="{obj.cover_image.url}" width="40" height="40"/></a>'
        )

    get_thumbnail.short_description = "Thumbnail"
