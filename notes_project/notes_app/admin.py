from django.contrib import admin
from notes_app.models import Note_model, Topic, Test
# Register your models here.

admin.site.register(Note_model)
admin.site.register(Topic)
admin.site.register(Test)
