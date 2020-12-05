from django.urls import path
from categories import views as categorie_views

app_name = "categories"

urlpatterns = [
    path("", categorie_views.home_view, name="home"),
    path("<int:pk>", categorie_views.CategoryDetail.as_view(), name="detail"),
]
