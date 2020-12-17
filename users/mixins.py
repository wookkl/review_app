# Django
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# locale Django
from . import models


class LoggedOutOnlyView(UserPassesTestMixin):

    """ Logged Out Only View Mixin Definition """

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Cant't go there")
        return redirect(reverse("core:home"))


class LoggedInOnlyView(LoginRequiredMixin):

    """ Logged In Onloy View Mixin Definition """

    login_url = reverse_lazy("core:login")

    def test_func(self):
        return self.request.user.is_authenticated


class EmailLogInOnlyView(UserPassesTestMixin):

    """ Email Log In Only View Mixin Definution"""

    permission_denied_message = "Page not found"

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.login_method == models.User.LOGIN_EMAIL

    def handle_no_permission(self):
        messages.error(self.request, "Cant't go there")
        return redirect(reverse("core:home"))