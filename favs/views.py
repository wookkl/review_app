from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse
from movies import models as movie_models
from books import models as book_models
from . import models


def toggle_favs(request, pk):

    """ Toggle favourite list Definition """

    _type = request.GET.get("type", None)
    action = request.GET.get("action", None)
    favlist, _ = models.FavList.objects.get_or_create(created_by=request.user)
    prev_url = request.META.get("HTTP_REFERER")
    if _type == "movie":
        try:
            movie = movie_models.Movie.objects.get(pk=pk)
        except movie_models.Movie.DoesNotExist:
            movie = None
        if movie is not None:
            if action == "add":
                favlist.movies.add(movie)
            elif action == "delete":
                favlist.movies.remove(movie)
            return redirect(prev_url)
    elif _type == "book":
        try:
            book = book_models.Book.objects.get(pk=pk)
        except book_models.Book.DoesNotExist:
            book = None
        if book is not None:
            if action == "add":
                favlist.books.add(book)
                print(favlist)
            elif action == "delete":
                favlist.books.remove(book)
        return redirect(prev_url)


class SeeFavsView(TemplateView):

    """ Favourite Lists View Definition """

    template_name = "favs/fav_detail.html"
