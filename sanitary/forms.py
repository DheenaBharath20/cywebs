from django import forms
from .models import Sanitary

class PostForm(forms.ModelForm):

    class Meta:
        model = Sanitary
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]