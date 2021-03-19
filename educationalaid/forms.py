from django import forms
from .models import Educationalaid

class PostForm(forms.ModelForm):

    class Meta:
        model = Educationalaid
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]