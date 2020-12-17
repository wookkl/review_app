# System Library
import os
import requests
import pprint
# Django
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, DetailView, UpdateView

# local Django
from users import forms, models, mixins


class LoginView(mixins.LoggedOutOnlyView, View):

    """ Login View Definition """

    def get(self, request):
        form = forms.LogInForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LogInForm(request.POST)
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


class GithubException(Exception):
    pass


def github_login(request):

    """ Github Log In Definition """
    client_id = os.environ.get("GITHUB_CLIENT_ID", None)
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&scope=read:user")


def github_callback(request):

    """ Github Callback Definition """

    try:
        client_id = os.environ.get("GITHUB_CLIENT_ID")
        client_secret = os.environ.get("GITHUB_SECRET")
        code = request.GET.get("code", None)
        if code:
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
                )
            token_json = token_request.json()
            access_token = token_json.get("access_token")
            profile_json = requests.get("https://api.github.com/user", headers={
                "Authorization": f"token {access_token}",
                "Accept": "application/json",
                }).json()
            user = profile_json.get("login", None)
            if user:
                name = profile_json.get("name")
                email = profile_json.get("email")
                bio = profile_json.get("bio")
                if bio is None:
                    bio = ""
                try:
                    user = models.User.objects.get(email=email)
                    if user.login_method != models.User.LOGIN_GITHUB:
                        # Does not matched login method
                        raise GithubException()
                except models.User.DoesNotExist:
                    user = models.User.objects.create(email=email,username=email, first_name=name, login_method=models.User.LOGIN_GITHUB, bio=bio)
                    user.set_unusable_password()
                    user.save()
                login(request, user)
                return redirect(reverse("core:home"))
            else:
                # Can't create user
                raise GithubException()
        else:
            # Can't get  code
            raise GithubException()
    except GithubException:
        return redirect(reverse("users:login"))


class KakaoException(Exception):
    pass


def kakao_login(request):
    client_id = os.environ.get("KAKAO_CLIENT_ID")
    redirect_uri = "http://app-review.eba-sn6bgenn.ap-northeast-2.elasticbeanstalk.com/users/login/kakao/callback/"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")


def kakao_callback(request):
    client_id = os.environ.get("KAKAO_CLIENT_ID")
    code = request.GET.get("code", None)
    redirect_uri = "http://app-review.eba-sn6bgenn.ap-northeast-2.elasticbeanstalk.com/users/login/kakao/callback/"
    if code is not None:
        post_uri = f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        content_type = "application/x-www-form-urlencoded;charset=utf-8"
        token_json = requests.post(post_uri, headers={"Content-type": content_type}).json()
        access_token = token_json.get("access_token", None)
        profile_json = requests.post("https://kapi.kakao.com/v2/user/me", headers={
                "Authorization": f"Bearer {access_token}",
                "Content-type": content_type,
                }).json()
        kakao_account = profile_json.get("kakao_account", None)

        if kakao_account is not None:
            email = kakao_account.get("email")
            name = kakao_account.get("profile").get("nickname", None)
            if name is None:
                name = ""
            try:
                user = models.User.objects.get(email=email)
                if user.login_method != models.User.LOGIN_KAKAO:
                    raise KakaoException()
            except models.User.DoesNotExist:
                user = models.User.objects.create(email=email, username=email, first_name=name, login_method=models.User.LOGIN_KAKAO)
                user.set_unusable_password()
                user.save()
            login(request, user)
            return redirect(reverse("core:home"))
    else:
        return redirect(reverse("users:login"))


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(mixins.LoggedOutOnlyView, FormView):

    """ SignUp View Definition """

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
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

    model = models.User

    context_object_name = "user_obj"


class UpdateUserView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    """ Update User View Definition """

    model = models.User
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
    mixins.LoggedInOnlyView, SuccessMessageMixin, PasswordChangeView, mixins.EmailLogInOnlyView
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
