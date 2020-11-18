from django.shortcuts import render


def IndexView(request):
    return render(request, "index.html")


def SearchView(request):
    return render(request, "search.html")