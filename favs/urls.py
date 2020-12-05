from django.urls import path
from favs import views

app_name = "favs"

urlpatterns = [
    path("toggle/<int:pk>/", views.toggle_favs, name="toggle-favs"),
    path("", views.SeeFavsView.as_view(), name="see-favs"),
]
