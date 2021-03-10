from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from urllib import request
from notes_app.forms import UserInfoForm, Accountform

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views import View


def index(request):
    return render(request, 'notes_app/index.html')


def create(request):
    bound_form = Noteform(request.POST)

    if bound_form.is_valid():
        new_form = bound_form.save()
        return redirect('index')

    return render(request, 'notes_app/create.html', {'form': bound_form})


def read(request):
    return render(request, 'notes_app/read.html')


def undo(request):
    note = Noteform(request.GET)
    return render(request, 'notes_app/undo.html', {'note': note})


def delete(request):
    # posts = Note_model.objects.all()
    # args = {'posts': posts}
    return render(request, 'notes_app/delete.html')


def test_update(request, num):
    # obj = Note_model.objects.get(id=num)

    if (request.GET.get('DeleteButton')):
        # Note_model.objects.filter(id=request.GET.get('DeleteButton')).delete()
        # return redirect('read')
        print("redirect read")
    return render(request, 'notes_app/test_update.html')


def update(request, num):
    # model = Note_model.objects.get(id=num)
    forma = Noteform()
    # context = {'form': model}
    return render(request, 'notes_app/update.html')


def userinfo(request):

    registered = False

    if request.method == 'POST':

        user_info = UserInfoForm(data=request.POST)

        if user_info.is_valid():
            user = user_info.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('userinfo')
    else:
        user_info = UserInfoForm()
    return render(request, 'notes_app/userinfo.html', {'user_info': user_info, 'registered': registered})


def register(request):
    bound_form = Accountform(request.POST)

    if bound_form.is_valid():
        _form = bound_form.save_account()
        return redirect('index')

    return render(request, 'notes_app/register.html', {'form': bound_form})

def user_login(request):

    if request.method == 'POST':
        # Take username and password data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Automatically authenticate user
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                #If the user is active we gona to log the user in
                login(request,user)
                #Then user loged in we send him to index:
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")           
            print(f"Username: {username} and password {password}")
    else:
        return render(request, 'notes_app/user_login.html')

    return render(request, 'notes_app/user_login.html')
