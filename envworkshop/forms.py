from django import forms
from .models import Envworkshop

class PostForm(forms.ModelForm):

    class Meta:
        model = Envworkshop
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]