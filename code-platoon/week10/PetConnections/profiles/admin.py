from django.contrib import admin # brings in the admin ability
from .models import Questionaire, User_Profile, Pet_Profile, Match # brings in your Post model from the models.py file


admin.site.register(Questionaire)
admin.site.register(User_Profile)
admin.site.register(Pet_Profile)
admin.site.register(Match)
