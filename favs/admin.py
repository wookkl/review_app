from django.contrib import admin
from . import models


@admin.register(models.Fav)
class FavAdmin(admin.ModelAdmin):

    """ Fav Admin Definition """