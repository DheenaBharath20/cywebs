from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Naturaldisaster
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Naturaldisaster
    template_name = 'Naturaldisaster.html'

class CreatePostView(CreateView):
    model = Naturaldisaster
    form_class = PostForm
    template_name = "Naturaldisaster-add.html"
    success_url = reverse_lazy("Naturaldisaster")