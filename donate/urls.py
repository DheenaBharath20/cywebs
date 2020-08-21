from django.urls import path
from donate import views

app_name = 'donate'
urlpatterns = [
    path('',views.donate, name='donate'),
]
