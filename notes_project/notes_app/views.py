from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django import forms
from urllib import request
from notes_app.forms import UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notes_app.forms import UserForm, UserProfileInfoForm
from django.views import View
from notes_app.models import ClassRoom
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'notes_app/index.html')

def create(request):
    # bound_form = Noteform(request.POST)

    # if bound_form.is_valid():
    #     # new_form = bound_form.save()
    #     return redirect('index')

    return render(request, 'notes_app/create.html')


def update(request, num):
    # model = Note_model.objects.get(id=num)
    # form = Noteform()
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
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # Grabing the user form and saving it to DB
            user = user_form.save()
            # Hashing the pasword
            user.set_password(user.password)
            user.save()

            # Don't commit to DB yet
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

                registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'notes_app/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Return something special for user


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


# def user_login(request):

#     if request.method == 'POST':
#         # Take username and password data
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Automatically authenticate user
#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 # If the user is active we gona to log the user in
#                 login(request, user)
#                 # Then user loged in we send him to index:
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Account not active")
#         else:
#             print("Someone tried to login and failed!")
#             print(f"Username: {username} and password {password}")
#     else:
#         return render(request, 'notes_app/user_login.html')

#     return render(request, 'notes_app/user_login.html')

# class Class_room(View):

# def class_room(request):
#     obj = ClassRoom.objects.all()
#     return render(request, 'notes_app/class_room.html', {'classes':obj})

class ClassRoomListView(ListView):
    model = ClassRoom


#By ID
class ClassRoomDetailView(DetailView):
    model = ClassRoom
    def get_context_data(self, **kwargs):
        context = {'obj': ClassRoom.objects.get(
            id=self.kwargs['pk'])}
        return context

class UserLogin(View):
    def get(self, request):
        return render(request, 'notes_app/user_login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            print("Someone tried to login and failed!")           
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Account not active")
        
        if not user.is_active:
            return HttpResponse("Account not active")
        
        login(request, user)
        return HttpResponseRedirect(reverse('index'))