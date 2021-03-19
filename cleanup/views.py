from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Cleanups
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Cleanups
    template_name = 'clean.html'

class CreatePostView(CreateView):
    model = Cleanups
    form_class = PostForm
    template_name = "clean-add.html"
    success_url = reverse_lazy("cleanups")