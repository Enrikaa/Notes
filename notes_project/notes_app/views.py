from django.shortcuts import render
from django.http import HttpResponse
from .models import Note_model, Topic
# Create your views here.

def index(request):
    return render(request,'notes_app/index.html')

def create(request):
    return render(request,'notes_app/create.html')

def read(request):
    data=Note_model.objects.all()
    return render(request,'notes_app/read.html',{'notes':data})

def undo(request):
    return render(request,'notes_app/undo.html')

def delete(request):
    return render(request,'notes_app/delete.html')