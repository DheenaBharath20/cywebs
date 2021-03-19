from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Schoolrestoration
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Schoolrestoration
    template_name = 'sklres.html'

class CreatePostView(CreateView):
    model = Schoolrestoration
    form_class = PostForm
    template_name = "sklres-add.html"
    success_url = reverse_lazy("schoolrestoration")