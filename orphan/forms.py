from django import forms
from .models import Orphan

class PostForm(forms.ModelForm):

    class Meta:
        model = Orphan
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]