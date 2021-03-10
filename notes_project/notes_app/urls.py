from django.conf.urls import url
from notes_app import views
from django.views.generic import ListView
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name='create'),
    url(r'^read/$', views.read, name='read'),
    url(r'^undo/$', views.undo, name='undo'),
    url(r'^delete/$', views.delete, name='delete'),
    path('test_update/<int:num>/', views.test_update, name='test_update'),
    path('update/<int:num>/', views.update, name='update'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
