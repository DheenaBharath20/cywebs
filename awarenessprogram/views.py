from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Awarenessprogram
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Awarenessprogram
    template_name = 'aware_prog.html'

class CreatePostView(CreateView):
    model = Awarenessprogram
    form_class = PostForm
    template_name = "aware_prog-add.html"
    success_url = reverse_lazy("awarenessprogram")