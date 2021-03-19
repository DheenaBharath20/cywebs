from django import forms
from .models import Wastemanagement

class PostForm(forms.ModelForm):

    class Meta:
        model = Wastemanagement
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]