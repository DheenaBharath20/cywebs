from django.urls import path
from .views import HomePageView,CreatePostView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'vidhaipom'),
    path('add/', CreatePostView.as_view(), name = 'add'),
]