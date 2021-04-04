from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Announcements
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Announcements
    template_name = 'announcement.html'

class CreatePostView(CreateView):
    model = Announcements
    form_class = PostForm
    template_name = "announcement-add.html"
    success_url = reverse_lazy("announcement")