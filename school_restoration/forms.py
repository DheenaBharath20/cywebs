from django import forms
from .models import Schoolrestoration

class PostForm(forms.ModelForm):

    class Meta:
        model = Schoolrestoration
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]