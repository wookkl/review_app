from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.messages.views import SuccessMessageMixin
from users import forms as user_forms
from users import models as user_models
from users import mixins as user_mixins


class LoginView(user_mixins.LoggedOutOnlyView, View):

    """ Login View Definition """

    def get(self, request):
        form = user_forms.LogInForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = user_forms.LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(user_mixins.LoggedOutOnlyView, FormView):

    """ SignUp View Definition """

    template_name = "users/signup.html"
    form_class = user_forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "wo",
        "last_name": "ki",
        "email": "wo@na.co",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse("core:home"))
        return super().form_valid(form)


class UserProfileView(DetailView):

    """ User Profile View Definition """

    model = user_models.User

    context_object_name = "user_obj"


class UpdateUserView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    """ Update User View Definition """

    model = user_models.User
    template_name = "users/update-profile.html"
    fields = (
        "email",
        "first_name",
        "last_name",
        "bio",
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        self.object.username = email
        self.object.save()
        return super().form_valid(form)


class UpdatePasswordView(
    user_mixins.LoggedInOnlyView, SuccessMessageMixin, PasswordChangeView
):

    """ Update Password View Definition """

    template_name = "users/update-password.html"
    success_message = "Password updated"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].widget.attrs = {"placeholder": "Current Password"}
        form.fields["new_password1"].widget.attrs = {"placeholder": "New Password"}
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "Confirm new Password"
        }
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()