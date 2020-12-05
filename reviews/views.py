from django.shortcuts import redirect, reverse
from books import models as book_models
from movies import models as movie_models
from . import forms


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
                review.book = movie
                review.created_by = request.user
                review.save()
                return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))
        elif _type == "book":
            try:
                book = book_models.book.objects.get(pk=pk)
            except book_models.book.DoesNotExist:
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
