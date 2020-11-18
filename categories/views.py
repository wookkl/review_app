from django.shortcuts import render


def home_view(request):
    return render(request, "categories/categories_home.html")
