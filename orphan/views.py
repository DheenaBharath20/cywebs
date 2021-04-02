from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Orphan
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Orphan
    template_name = 'Orphan.html'

class CreatePostView(CreateView):
    model = Orphan
    form_class = PostForm
    template_name = "Orphan-add.html"
    success_url = reverse_lazy("Orphan")