# Django
from django import template

# local Django
from favs import models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, _type, book_or_movie):
    user = context.request.user
    try:
        fav = models.FavList.objects.get(created_by=user)
    except models.FavList.DoesNotExist:
        fav = None
    if fav is not None:
        if _type == "movie":
            return book_or_movie in fav.movies.all()
        elif _type == "book":
            return book_or_movie in fav.books.all()
