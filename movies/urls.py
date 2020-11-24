from django.urls import path
from movies import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.MovieList.as_view(), name="home"),
    path("<int:pk>/", movie_views.MovieDetail.as_view(), name="detail"),
]
