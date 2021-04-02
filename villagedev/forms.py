from django import forms
from .models import VillageDevelopment

class PostForm(forms.ModelForm):

    class Meta:
        model = VillageDevelopment
        fields = ['title', 'img1', 'img2', 'img3', 'img4', 'date', 'location' ]