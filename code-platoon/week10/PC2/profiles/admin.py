from django.contrib import admin # brings in the admin ability
from .models import Questionaire, User, Pet, Match # brings in your Post model from the models.py file


admin.site.register(Questionaire)
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Match)
