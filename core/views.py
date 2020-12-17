# Django
from django.shortcuts import render

# local Django
from people import models as person_models
from movies import models as movie_models
from books import models as book_models
from categories import models as category_models


def home_view(request):

    """ Home View Definition """

    movies = movie_models.Movie.objects.all().order_by("-pk")[:10]
    books = book_models.Book.objects.all().order_by("-pk")[:10]
    people = person_models.Person.objects.all().order_by("-pk")[:10]

    return render(
        request,
        "home.html",
        {
            "movies": movies,
            "books": books,
            "people": people,
        },
    )


def search_view(request):

    term = request.GET.get("search")

    movies = books = people = None

    if term:
        movies = movie_models.Movie.objects.filter(title__startswith=term)
        books = book_models.Book.objects.filter(title__startswith=term)
        people = person_models.Person.objects.filter(name__startswith=term)

        print(movies, books, people)

    return render(
        request,
        "search.html",
        {
            "categories": category_models.Category.objects.all(),
            "movies": movies,
            "books": books,
            "term": term,
            "people": people,
        },
    )
