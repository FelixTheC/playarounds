from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from matrix.forms import LoginForm
from matrix.forms import RegisterForm


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, template_name="login.html", context={"login_form": login_form})
    else:
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(request,
                                username=login_form.cleaned_data["username"],
                                password=login_form.cleaned_data["password"])
            if user:
                login(user)
            else:
                return redirect(reverse("matrix_register"))


def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return get_register_user(request)
    else:
        return post_register_user(request)


def get_register_user(request: HttpRequest):
    register_form = RegisterForm()
    return render(request,
                  template_name="register.html",
                  context={"register_form": register_form})


def post_register_user(request: HttpRequest):
    register_form = RegisterForm(data=request.POST)
    if register_form.is_valid():
        username_email = register_form.cleaned_data["username"]
        User.objects.create_user(username=username_email,
                                 email=username_email,
                                 password=register_form.cleaned_data["password"])
        return redirect(reverse("matrix_login"))


def logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse("matrix_login"))
