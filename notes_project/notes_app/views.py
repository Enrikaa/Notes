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
    error=''
    print("START METHOD")
    
    if request.method=='POST':
        print('start post')
        # data = request.POST.get('title')
        # print(data)
        form=Noteform()
        print('create Note obj')
        print(request.POST.get('title'))
        print(request.POST.get('category'))
        print(request.POST.get('note_text'))
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('index')
            # return render(request,'notes_app/index.html')
        else:
            error='Bad input!'
            print("GET Error")
            form.save()

    form=Noteform()
    content={
        'form':form,
        'error':error
    }
    return render(request,'notes_app/create.html',content)



def read(request):
    data=Note_model.objects.all()
    return render(request, 'notes_app/read.html',{'notes':data})

def undo(request):
    return render(request,'notes_app/undo.html')

def delete(request):
    return render(request,'notes_app/delete.html')