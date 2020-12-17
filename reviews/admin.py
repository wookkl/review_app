# Django
from django.contrib import admin

# local Django
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_display = (
        "created_by",
        "text",
        "movie",
        "book",
        "rating",
    )

    list_filter = (
        "created_by",
        "movie",
        "book",
    )
