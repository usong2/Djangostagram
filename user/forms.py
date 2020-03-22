from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password

class Loginform(forms.Form):
    user_id = forms.CharField(max_length=32, label="아이디")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")