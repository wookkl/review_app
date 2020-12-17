# Django
from django.urls import path

# local Django
from categories import views

app_name = "categories"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("<int:pk>", views.CategoryDetail.as_view(), name="detail"),
]
