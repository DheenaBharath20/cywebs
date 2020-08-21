from django.urls import path
from .views import HomePageView, CreatePostView


urlpatterns=[
    path('', HomePageView.as_view(), name='others'),
    path('add/', CreatePostView.as_view(), name='add'),
]