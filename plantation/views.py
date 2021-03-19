from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Plantation
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Plantation
    template_name = 'plant.html'

class CreatePostView(CreateView):
    model = Plantation
    form_class = PostForm
    template_name = "plant-add.html"
    success_url = reverse_lazy("plantation")