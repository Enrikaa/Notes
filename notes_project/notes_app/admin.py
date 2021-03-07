from django.contrib import admin
from notes_app.models import Note_model, Account, UserInfo
# Register your models here.

admin.site.register(Note_model)
admin.site.register(Account)
admin.site.register(UserInfo)
