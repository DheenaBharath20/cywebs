from django.urls import path
from .views import HomePageView, CreatePostView


urlpatterns=[
    path('', HomePageView.as_view(), name='schoolrestoration'),
    path('add/', CreatePostView.as_view(), name='add_sklres'),
]