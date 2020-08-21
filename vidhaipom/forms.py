from django import forms
from .models import Vidhaipom

class PostForm(forms.ModelForm):
    class Meta:
        model = Vidhaipom
        fields = ['title','img1', 'img2', 'content', 'date']