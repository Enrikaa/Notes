from django.db import models

# Create your models here.
class Note_model(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150,unique=True)
    title = models.CharField(max_length=100,unique=True)
    note_text = models.CharField(max_length=20000)

    def __str__(self):
        return self.title