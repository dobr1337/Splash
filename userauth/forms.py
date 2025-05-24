from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AuthForm(forms.Form):
    login = forms.CharField(max_length=150)
    password = forms.CharField()

    def clean_password(self):
        password = self.cleaned_data.get("password")
        username = self.cleaned_data.get("login")
        user = authenticate(username=username, password=password)

        if user is None:
            raise forms.ValidationError("Неверные данные")
        return password
