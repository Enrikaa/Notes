from .models import Note_model, Account
from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError
from notes_app.models import UserInfo
from django.contrib.auth.models import User

class Noteform(forms.Form):
    category = forms.CharField(max_length=264)
    title = forms.CharField(max_length=264)
    note_text = forms.CharField(max_length=264)

    category.widget.attrs.update({'class': 'form-control'})
    title.widget.attrs.update({'class': 'form-control'})
    note_text.widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        new_title = self.cleaned_data['title'].lower()
        if new_title == 'create':
            raise ValidationError('Title may not be "Create"')
        return new_title

    def save(self):
        new_note = Note_model.objects.create(
            category=self.cleaned_data['category'],
            title=self.cleaned_data['title'],
            note_text=self.cleaned_data['note_text'],
        )
        return new_note

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class Accountform(forms.Form):
    name = forms.CharField(max_length=264)
    username = forms.CharField(max_length=264)
    gender = forms.CharField(max_length=264)
    age = forms.CharField(max_length=264)

    name.widget.attrs.update({'class': 'form-control'})
    username.widget.attrs.update({'class': 'form-control'})
    gender.widget.attrs.update({'class': 'form-control'})
    age.widget.attrs.update({'class': 'form-control'})

    def save_account(self):
        new_account = Account.objects.create(
            name=self.cleaned_data['name'],
            username=self.cleaned_data['username'],
            gender=self.cleaned_data['gender'],
            age=self.cleaned_data['age'],
        )
        return new_account
