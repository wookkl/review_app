from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from users import forms as user_forms


class LoginView(View):

    """ Login View Definition """

    def get(self, request):
        form = user_forms.LoginForm(initial={"email": "qwfq@nae.c"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = user_forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))