from django import forms
from .models import Tuitioncentre

class PostForm(forms.ModelForm):

    class Meta:
        model = Tuitioncentre
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]