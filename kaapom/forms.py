from django import forms
from .models import Kaapom

class PostForm(forms.ModelForm):

    class Meta:
        model = Kaapom
        fields = ['title', 'img1', 'img2', 'content', 'date']