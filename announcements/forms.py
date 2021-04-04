from django import forms
from .models import Announcements

class PostForm(forms.ModelForm):

    class Meta:
        model = Announcements
        fields = ['title', 'content', 'date', 'url' ]