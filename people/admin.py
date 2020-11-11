from django.contrib import admin
from . import models


@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):

    """ People Admin Definition """