from django.urls import path
from core import views as core_views
from users import views as user_views


app_name = "core"

urlpatterns = [
    path("", core_views.HomeView, name="home"),
    path("search/", core_views.SearchView, name="search"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", user_views.log_out, name="logout"),
]
