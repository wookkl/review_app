from django.shortcuts import render


def home_view(request):
    return render(request, "movies/movies_home.html")
