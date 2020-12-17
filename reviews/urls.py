# Django
from django.urls import path

# local Django
from . import views

app_name = "reviews"
urlpatterns = [
    path("create/<int:pk>/", views.create_review, name="create"),
    path("delete/<int:pk>/", views.delete_review, name="delete"),
    path("write/<int:pk>/", views.ReviewFormView.as_view(), name="write"),
]