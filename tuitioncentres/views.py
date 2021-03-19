from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Tuitioncentre
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Tuitioncentre
    template_name = 'tuition.html'

class CreatePostView(CreateView):
    model = Tuitioncentre
    form_class = PostForm
    template_name = "tuition-add.html"
    success_url = reverse_lazy("tuitioncentres")