from django import forms
from .models import Naturaldisaster

class PostForm(forms.ModelForm):

    class Meta:
        model = Naturaldisaster
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]