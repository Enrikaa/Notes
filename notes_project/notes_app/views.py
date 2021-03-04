from django.shortcuts import render, redirect
from django.http import HttpResponse
from notes_app.forms import Noteform
from django import forms
from urllib import request
from notes_app.models import Note_model
# Create your views here.


def index(request):
    return render(request, 'notes_app/index.html')


def create(request):
    bound_form = Noteform(request.POST)

    if bound_form.is_valid():
        new_form = bound_form.save()
        return redirect('index')

    return render(request, 'notes_app/create.html', {'form': bound_form})


def read(request):
    data = Note_model.objects.all()
    return render(request, 'notes_app/read.html', {'notes': data})


def undo(request):
    note = Noteform(request.GET)
    return render(request, 'notes_app/undo.html', {'note': note})


def delete(request):
    posts = Note_model.objects.all()

    args = {'posts': posts}
    return render(request, 'notes_app/delete.html', context=args)
