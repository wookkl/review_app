# Django
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# local Django
from movies import models as movie_models
from users import mixins as user_mixins


class MovieList(ListView):

    """ Movie List View Definition """

    model = movie_models.Movie
    paginate_by = 10
    paginate_orphans = 5
    template_name = "movies/list.html"
    ordering = "-created"

    def get_context_data(self, **kwargs):
        try:
            return super(MovieList, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(MovieList, self).get_context_data(**kwargs)


class MovieDetail(DetailView):

    """ Movie Detail Definition """

    model = movie_models.Movie
    template_name = "movies/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["pk"] = pk
        return context


class MovieEdit(user_mixins.LoggedInOnlyView, UpdateView):

    """ Movie Edit View Definition """

    model = movie_models.Movie
    template_name = "movies/edit.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "category",
        "director",
        "cast",
    )


class MovieCreate(user_mixins.LoggedInOnlyView, CreateView):

    """ Movie Create View Definition """

    model = movie_models.Movie
    template_name = "movies/create.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "category",
        "director",
        "cast",
    )
