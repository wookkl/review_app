from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavAdmin(admin.ModelAdmin):

    """ Fav Admin Definition """
