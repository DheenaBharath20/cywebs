from django import forms
from .models import Greenclub

class PostForm(forms.ModelForm):

    class Meta:
        model = Greenclub
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]