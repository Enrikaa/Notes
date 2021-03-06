from django.conf.urls import url
from notes_app import views
from django.views.generic import ListView
from notes_app.models import Note_model
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name='create'),
    url(r'^read/$', views.read, name='read'),
    url(r'^undo/$', views.undo, name='undo'),
    url(r'^delete/$', views.delete, name='delete'),
    path('test_update/<int:num>/', views.test_update, name='test_update'),
    path('test_update2/<int:num>/', views.test_update2, name='test_update2'),
    url(r'^read2/$', views.read2, name='read2'),
]
