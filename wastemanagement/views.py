from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Wastemanagement
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Wastemanagement
    template_name = 'waste.html'

class CreatePostView(CreateView):
    model = Wastemanagement
    form_class = PostForm
    template_name = "waste-add.html"
    success_url = reverse_lazy("wastemanagement")