from django.views.generic import ListView, CreateView
from .models import Others
from django.urls import reverse_lazy
from .forms import PostForm


# Create your views here.
class HomePageView(ListView):
    model = Others
    template_name = 'others.html'

class CreatePostView(CreateView):
    model = Others
    form_class = PostForm
    template_name = 'others-add.html'
    success_url = reverse_lazy('others')
