from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import VillageDevelopment
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = VillageDevelopment
    template_name = 'villagedev.html'

class CreatePostView(CreateView):
    model = VillageDevelopment
    form_class = PostForm
    template_name = "villagedev-add.html"
    success_url = reverse_lazy("VillageDevelopment")