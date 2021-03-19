from django import forms
from .models import Awarenessprogram

class PostForm(forms.ModelForm):

    class Meta:
        model = Awarenessprogram
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]