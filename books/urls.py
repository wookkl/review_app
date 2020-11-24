from django.urls import path
from books import views as book_views

app_name = "books"

urlpatterns = [
    path("", book_views.BookList.as_view(), name="home"),
    path("<int:pk>/", book_views.BookDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", book_views.BookEdit.as_view(), name="edit"),
    path("create/", book_views.BookCreate.as_view(), name="create"),
]
