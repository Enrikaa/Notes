from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'notes_app/index.html')

def create(request):
    return render(request,'notes_app/create.html')

def read(request):
    return render(request,'notes_app/read.html')

def undo(request):
    return render(request,'notes_app/undo.html')

def delete(request):
    return render(request,'notes_app/delete.html')