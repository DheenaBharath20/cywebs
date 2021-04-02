from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Sanitary
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Sanitary
    template_name = 'sanitary.html'

class CreatePostView(CreateView):
    model = Sanitary
    form_class = PostForm
    template_name = "sanitary-add.html"
    success_url = reverse_lazy("sanitary")