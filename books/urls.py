# Django
from django.urls import path

# local Django
from books import views

app_name = "books"

urlpatterns = [
    path("", views.BookList.as_view(), name="home"),
    path("<int:pk>/", views.BookDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.BookEdit.as_view(), name="edit"),
    path("create/", views.BookCreate.as_view(), name="create"),
]
