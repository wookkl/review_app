from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from people import models as person_models
from movies import models as movie_models
from books import models as book_models


def HomeView(request):
    movie_querysets = movie_models.Movie.objects.all().order_by("pk")
    book_querysets = book_models.Book.objects.all().order_by("pk")
    person_querysets = person_models.Person.objects.all().order_by("pk")
    try:
        movie_paginator = Paginator(movie_querysets, 10, orphans=5)
        book_paginator = Paginator(book_querysets, 10, orphans=5)
        person_paginator = Paginator(person_querysets, 10, orphans=5)
        movies = movie_paginator.page(1)
        books = book_paginator.page(1)
        people = person_paginator.page(1)
        return render(
            request,
            "home.html",
            {
                "movies": movies,
                "books": books,
                "people": people,
            },
        )
    except InvalidPage:
        return redirect("/")


def SearchView(request):
    return render(request, "search.html")