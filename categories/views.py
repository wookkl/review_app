from django.shortcuts import render
from django.views.generic import DetailView
from categories.models import Category


def home_view(request):
    return render(request, "categories/categories_home.html")


class CategoryDetail(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"
