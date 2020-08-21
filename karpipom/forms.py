from django import forms
from .models import Karpipom

class PostForm(forms.ModelForm):
    class Meta:
        model = Karpipom
        fields = ['title','img1', 'img2', 'content', 'date']