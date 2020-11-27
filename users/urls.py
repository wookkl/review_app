from django.urls import path
from users import views as user_views


app_name = "users"

urlpatterns = [
    path("<int:pk>/", user_views.UserProfileView.as_view(), name="profile"),
]
