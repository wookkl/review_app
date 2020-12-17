# Django
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# local Django
from books import models as book_models
from users import mixins as user_mixins


class BookList(ListView):

    """ Book List View Definition """

    model = book_models.Book
    paginate_by = 10
    paginate_orphans = 5
    template_name = "books/list.html"
    ordering = "-created"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["pk"] = pk
        return context


class BookEdit(user_mixins.LoggedInOnlyView, UpdateView):

    """ Book Edit View Definition """

    model = book_models.Book
    template_name = "books/edit.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
    )

    def get_object(self, queryset=None):
        book = super().get_object(queryset=queryset)
        if self.request.user.is_staff:
            return book
        else:
            raise Http404()


class BookCreate(user_mixins.LoggedInOnlyView, CreateView):

    """ Book Create View Definition """

    model = book_models.Book
    template_name = "books/create.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "category",
        "writer",
    )

    def get_object(self, queryset=None):
        book = super().get_object(queryset=queryset)
        if self.request.user.is_staff:
            return book
        else:
            raise Http404()
