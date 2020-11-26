from django import forms
from users import models as user_models


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = user_models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except user_models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("user does not exist"))


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user_models.User.objects.get(email=email)
            raise forms.ValidationError("User already exist with that email")
        except user_models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            password1

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = user_models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()