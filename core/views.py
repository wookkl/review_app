from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from people import models as person_models
from movies import models as movie_models
from books import models as book_models


def HomeView(request):
    page = request.GET.get("page", 1)
    movie_querysets = movie_models.Movie.objects.all().order_by("pk")
    book_querysets = book_models.Book.objects.all().order_by("pk")
    person_querysets = person_models.Person.objects.all().order_by("pk")
    try:
        movie_paginator = Paginator(movie_querysets, 10, orphans=5)
        book_paginator = Paginator(book_querysets, 10, orphans=5)
        person_paginator = Paginator(person_querysets, 10, orphans=5)
        movies = movie_paginator.page(page)
        books = book_paginator.page(page)
        people = person_paginator.page(page)
        prev_page = (
            movies.has_previous() or books.has_previous() or people.has_previous()
        )
        next_page = movies.has_next() or books.has_next() or people.has_next()
        return render(
            request,
            "home.html",
            {
                "movie_page": movies,
                "book_page": books,
                "person_page": people,
                "current_page": page,
                "has_prev_page": prev_page,
                "has_next_page": next_page,
            },
        )
    except InvalidPage:
        return redirect("/")


def SearchView(request):
    return render(request, "search.html")