from .models import Karpipom
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.
class HomePageView(ListView):
    model = Karpipom
    template_name = 'karpipom.html'

class CreatePostView(CreateView):
    model = Karpipom
    form_class = PostForm
    template_name = 'add.html'
    success_url = reverse_lazy('karpipom')
