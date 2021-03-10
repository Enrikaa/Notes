# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_project.settings")

# import django

# django.setup()

# from notes_app.models import Note_model
# from faker import Faker
# import random

# fakegen = Faker()


# def add_cat():
#     categories = ["Python", "Java", "C++", "JavaScript", "PHP"]
#     t = random.choice(categories)
#     return t


# def add_data(N):

#     for entry in range(N):

#         cat_data = add_cat()
#         tit_data = fakegen.company()
#         not_data = fakegen.text()

#         t = Note_model(category=cat_data, title=tit_data, note_text=not_data)
#         t.save()
#         # return t


# if __name__ == "__main__":
#     print("Populating script!")
#     add_data(20)
#     print("Populating complete!")