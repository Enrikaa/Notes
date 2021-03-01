from django.conf.urls import url
from notes_app import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    
]