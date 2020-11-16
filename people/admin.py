from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    """ Person Admin Definition """

    list_display = (
        "name",
        "get_thumbnail",
        "kind",
    )

    list_filter = (
        "name",
        "kind",
    )

    def get_thumbnail(self, obj):
        print(obj.photo.url)
        return mark_safe(
            f'<a href="{obj.cover_image.url}"><img src="{obj.cover_image.url}" width="40" height="40"/></a>'
        )

    get_thumbnail.short_description = "Thumbnail"
