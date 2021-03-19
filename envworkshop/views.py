from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Envworkshop
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Envworkshop
    template_name = 'envwork.html'

class CreatePostView(CreateView):
    model = Envworkshop
    form_class = PostForm
    template_name = "envwork-add.html"
    success_url = reverse_lazy("envworkshop")