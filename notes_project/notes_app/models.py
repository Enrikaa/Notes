from django.db import models

# Create your models here.


class Note_model(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=264)
    title = models.CharField(max_length=264, unique=True)
    note_text = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.id


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264)
    username = models.CharField(max_length=264)
    gender = models.CharField(max_length=264)
    age = models.CharField(max_length=264)

    def __str__(self):
        return str(self.id)
