from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Educationalaid
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Educationalaid
    template_name = 'eduaid.html'

class CreatePostView(CreateView):
    model = Educationalaid
    form_class = PostForm
    template_name = "eduaid-add.html"
    success_url = reverse_lazy("educationalaid")