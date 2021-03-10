from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError
from notes_app.models import UserInfo
from django.contrib.auth.models import User
from notes_app.models import UserProfileInfo


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
