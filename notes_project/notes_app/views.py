from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note_model
from .forms import Noteform
from django import forms
from urllib import request
# Create your views here.

def index(request):
    return render(request,'notes_app/index.html')

def create(request):
    bound_form=Noteform(request.POST)

    if bound_form.is_valid():
        new_form=bound_form.save()
        return redirect('index')
        
    return render(request,'notes_app/create.html',{'form':bound_form})   

def read(request):
    data=Note_model.objects.all()
    return render(request, 'notes_app/read.html',{'notes':data})

def undo(request):
    return render(request,'notes_app/undo.html')

def delete(request):
    return render(request,'notes_app/delete.html')
