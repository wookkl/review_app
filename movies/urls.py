# Django
from django.urls import path

# local Django
from movies import views

app_name = "movies"

urlpatterns = [
    path("", views.MovieList.as_view(), name="home"),
    path("<int:pk>/", views.MovieDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.MovieEdit.as_view(), name="edit"),
    path("create/", views.MovieCreate.as_view(), name="create"),
]
