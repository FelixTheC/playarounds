#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from matrix.views import login, register_user, logout


urlpatterns = [
    path("login", login, name="matrix_login"),
    path("register", register_user, name="matrix_register"),
    path("logout", logout, name="matrix_logout"),
]
