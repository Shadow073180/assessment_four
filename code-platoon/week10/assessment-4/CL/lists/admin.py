from django.contrib import admin # brings in the admin ability
from .models import Post, Catagory# brings in your Post model from the models.py file

admin.site.register(Post)
admin.site.register(Catagory) # reg
