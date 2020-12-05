from django import template
from favs import models as fav_models
from movies import models as movie_models
from books import models as book_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, _type, book_or_movie):
    user = context.request.user
    try:
        fav = fav_models.FavList.objects.get(created_by=user)
    except fav_models.FavList.DoesNotExist:
        fav = None
    if fav is not None:
        if _type == "movie":
            return book_or_movie in fav.movies.all()
        elif _type == "book":
            return book_or_movie in fav.movies.all()
