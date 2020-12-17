# Django
from django.shortcuts import render
from django.views.generic import DetailView

# local Django
from categories.models import Category


def home_view(request):

    """ Home View Definition"""

    return render(request, "categories/categories_home.html")


class CategoryDetail(DetailView):

    """ Category Detail View Definition """

    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"
