from .models import Kaapom
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm

class HomePageView(ListView):
    model = Kaapom
    template_name = 'kaapom.html'
# Create your views here.

class CreatePageView(CreateView):
    model = Kaapom
    form_class = PostForm
    template_name = 'kaapom-add.html'
    success_url = reverse_lazy('kaapom')