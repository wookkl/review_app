from django.shortcuts import render
from people import models as person_models
from movies import models as movie_models
from books import models as book_models


def HomeView(request):
    movies = movie_models.Movie.objects.all().order_by("pk")[:10]
    books = book_models.Book.objects.all().order_by("pk")[:10]
    people = person_models.Person.objects.all().order_by("pk")[:10]

    return render(
        request,
        "home.html",
        {
            "movies": movies,
            "books": books,
            "people": people,
        },
    )


def SearchView(request):
    return render(request, "search.html")
