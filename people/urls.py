# Django
from django.urls import path

# local Django
from people import views

app_name = "people"

urlpatterns = [
    path("", views.PersonList.as_view(), name="home"),
    path("<int:pk>/", views.PersonDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PersonEdit.as_view(), name="edit"),
    path("create/", views.PersonCreate.as_view(), name="create"),
]
