from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from userauth.forms import AuthForm


def user_auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        username = request.POST.get("login", "")
        password = request.POST.get("password", "")

        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                print(f"Пользователь {username} вошел в аккаунт")
                return redirect("/")
            else:
                print(request, "Неправильный логин или пароль.")
        else:
            print(
                f"Форма авторизации не валидна. Введенные данные: логин='{username}', пароль='{password}'. "
                "Возможно, логин/пароль не прошли валидацию."
            )
        return render(request, "userauth/auth.html", {"form": form})

    else:
        form = AuthForm()
        return render(request, "userauth/auth.html", {"form": form})
