#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=128, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.EmailField(required=True, initial="example: jon.doe@doe.com")

    password = forms.CharField(required=True, max_length=128, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, max_length=128, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        usrname = cleaned_data["username"]
        passwd = cleaned_data["password"]
        passwd_check = cleaned_data["confirm_password"]

        if passwd != passwd_check and usrname != passwd_check and usrname != passwd_check:
            self.add_error("password", "Passwords are not identically")
            self.add_error("confirm_password", "Passwords are not identically")
