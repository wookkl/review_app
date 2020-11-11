from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    """ Person Admin Definition """

    list_display = (
        "name",
        "kind",
    )

    list_filter = (
        "name",
        "kind",
    )