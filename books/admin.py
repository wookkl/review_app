from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """ Book Admin Definition """

    list_display = (
        "title",
        "year",
        "writer",
        "rating",
    )

    list_filter = ("category", "writer")