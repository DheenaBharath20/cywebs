from django import forms
from .models import Cleanups

class PostForm(forms.ModelForm):

    class Meta:
        model = Cleanups
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]