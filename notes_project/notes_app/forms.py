from .models import Note_model
from django.forms import ModelForm, TextInput
from django import forms
from django.core.exceptions import ValidationError


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
