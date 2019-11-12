from django import forms
from .models import Catagory, Post 

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ('id', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('id', 'catagory', 'post_text')

