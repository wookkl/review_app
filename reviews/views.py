from django.views.generic import FormView
from django.shortcuts import redirect, reverse
from books import models as book_models
from movies import models as movie_models
from . import forms, models


def delete_review(request, pk):
    if request.method == "GET":
        models.Review.objects.filter(pk=pk).delete()
        return redirect(request.META.get("HTTP_REFERER"))


def create_review(request, pk):
    if request.method == "POST":
        _type = request.GET.get("type")
        form = forms.CreateReviewForm(request.POST)
        if _type == "movie":
            try:
                movie = movie_models.Movie.objects.get(pk=pk)
            except movie_models.Movie.DoesNotExist:
                movie = None
            if movie is None:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.movie = movie
                review.created_by = request.user
                review.save()
                return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))
        elif _type == "book":
            try:
                book = book_models.Book.objects.get(pk=pk)
            except book_models.Book.DoesNotExist:
                book = None
            if book is None:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.book = book
                review.created_by = request.user
                review.save()
                return redirect(reverse("books:detail", kwargs={"pk": book.pk}))
    return redirect(reverse("core:home"))


class ReviewFormView(FormView):

    """ Review Form Definition """

    template_name = "reviews/review_form.html"
    form_class = forms.CreateReviewForm

    def get_context_data(self, **kwargs):
        _type = self.request.GET.get("type")

        context = super(ReviewFormView, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs["pk"]
        if _type == "movie":
            context["type"] = _type
        elif _type == "book":
            context["type"] = _type
        return context
