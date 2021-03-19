from django.urls import path
from home.views import education, environment, home, socialwelfare


app_name = 'home'

urlpatterns = [
    path('edu/',education, name='edu'),
    path('',home, name='home'),
    path('env/',environment, name='env'),
    path('soc/',socialwelfare, name='socwel'),
]
