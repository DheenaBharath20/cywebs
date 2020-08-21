from django import forms
from .models import Others

class PostForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = ['title','img1', 'img2', 'content', 'date']