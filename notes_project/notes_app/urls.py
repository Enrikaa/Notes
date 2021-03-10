from django.conf.urls import url
from notes_app import views
from django.views.generic import ListView
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'special/', views.special, name='special'),
]
