from django.http import Http404
from django.views.generic import ListView
from django.views.generic import DetailView
from books import models as book_models


class BookList(ListView):

    """ Book List View Definition """

    model = book_models.Book
    paginate_by = 10
    paginate_orphans = 5
    template_name = "books/list.html"
    ordering = ("pk",)

    def get_context_data(self, **kwargs):
        try:
            return super(BookList, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(BookList, self).get_context_data(**kwargs)


class BookDetail(DetailView):

    """ Book Detail Definition """

    model = book_models.Book
    template_name = "books/detail.html"
