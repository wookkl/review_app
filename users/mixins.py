# Django
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    """ Logged Out Onloy View Mixin Definition """

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
