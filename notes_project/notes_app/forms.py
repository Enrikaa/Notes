from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError
from notes_app.models import UserInfo
from django.contrib.auth.models import User


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
