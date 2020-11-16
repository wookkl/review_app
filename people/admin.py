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
        try:
            return mark_safe(
                f'<a href="{obj.photo.url}"><img src="{obj.photo.url}" width="40" height="40"/></a>'
            )
        except Exception:
            return ""

    get_thumbnail.short_description = "Thumbnail"
