from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Skilldevprog
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Skilldevprog
    template_name = 'skilldev.html'

class CreatePostView(CreateView):
    model = Skilldevprog
    form_class = PostForm
    template_name = "skilldev-add.html"
    success_url = reverse_lazy("skilldevprog")