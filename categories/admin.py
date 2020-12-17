# Django
from django.contrib import admin

# local Django
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """ Category Admin Definition """

    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
