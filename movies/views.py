from django.shortcuts import render
from django.views.generic import ListView
from movies import models as movie_models


class MovieListView(ListView):

    """ Movie List View Definition """

    model = movie_models.Movie
    paginate_by = 10
    paginate_orphans = 5
    template_name = "movies/movies_list.html"
    ordering = ("pk",)
