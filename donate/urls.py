from django.urls import path, include
from donate import views

app_name = 'donate'
urlpatterns = [
    path('',views.donate, name='donate'),

]
