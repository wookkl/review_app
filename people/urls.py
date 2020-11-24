from django.urls import path
from people import views as person_views

app_name = "people"

urlpatterns = [
    path("", person_views.PersonList.as_view(), name="home"),
    path("<int:pk>/", person_views.PersonDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", person_views.PersonEdit.as_view(), name="edit"),
]
