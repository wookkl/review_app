# Django
from django.urls import path

# local Django
from users import views


app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("update-profile", views.UpdateUserView.as_view(), name="update"),
    path("update-password", views.UpdatePasswordView.as_view(), name="password"),
]
