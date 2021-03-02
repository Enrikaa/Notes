from .models import Note_model
from django.forms import ModelForm,TextInput
from django import forms

class Noteform(ModelForm):
    class Meta:
        model=Note_model
        fields=['title','category','note_text']
        widgets={
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Write title'
                }),
                'category':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Write category'
                }),
                'note_text':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Write note text'
                }),
        }
