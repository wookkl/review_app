from django.http import Http404
from django.views.generic import ListView
from movies import models as movie_models


class MovieListView(ListView):

    """ Movie List View Definition """

    model = movie_models.Movie
    paginate_by = 10
    paginate_orphans = 5
    template_name = "movies/movies_list.html"
    ordering = ("pk",)

    def get_context_data(self, **kwargs):
        try:
            return super(MovieListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(MovieListView, self).get_context_data(**kwargs)