# Generated by Django 3.1.7 on 2021-03-02 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]