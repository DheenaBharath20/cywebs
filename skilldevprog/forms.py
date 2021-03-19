from django import forms
from .models import Skilldevprog

class PostForm(forms.ModelForm):

    class Meta:
        model = Skilldevprog
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]