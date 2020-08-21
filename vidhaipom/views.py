from django.views.generic import ListView, CreateView
from .models import Vidhaipom
from django.urls import reverse_lazy
from .forms import PostForm


# Create your views here.
class HomePageView(ListView):
    model = Vidhaipom
    template_name = 'vidhaipom.html'

class CreatePostView(CreateView):
    model = Vidhaipom
    form_class = PostForm
    template_name = 'vidhaipom-add.html'
    success_url = reverse_lazy('home')