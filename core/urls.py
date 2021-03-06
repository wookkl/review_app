# Django
from django.urls import path

# local Django
from core import views as core_views
from users import views as user_views


app_name = "core"

urlpatterns = [
    path("", core_views.home_view, name="home"),
    path("search/", core_views.search_view, name="search"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", user_views.log_out, name="logout"),
    path("signup/", user_views.SignUpView.as_view(), name="signup"),
]
