from django.urls import path
from .views import HomePageView,CreatePageView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'kaapom'),
    path('add/', CreatePageView.as_view(), name = 'add')
]