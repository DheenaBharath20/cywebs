from django import forms
from .models import Plantation

class PostForm(forms.ModelForm):

    class Meta:
        model = Plantation
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]