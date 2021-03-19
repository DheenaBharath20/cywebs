from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Greenclub
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Greenclub
    template_name = 'greenclub.html'

class CreatePostView(CreateView):
    model = Greenclub
    form_class = PostForm
    template_name = "greenclub-add.html"
    success_url = reverse_lazy("greenclub")