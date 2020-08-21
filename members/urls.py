from django.urls import path
from members import views

app_name = 'members'
urlpatterns = [
    path('',views.members, name='members'),
]
