"""cywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('educationalaid/', include('educationalaid.urls')),
    path('awarenessprogram/', include('awarenessprogram.urls')),
    path('tuitioncentres/',include('tuitioncentres.urls')),
    path('skilldevprog/',include('skilldevprog.urls')),
    path('plantation/', include('plantation.urls')),
    path('greenclub/', include('greenclub.urls')),
    path('wastemanagement/', include('wastemanagement.urls')),
    path('cleanup/', include('cleanup.urls')),
    path('envworkshop/', include('envworkshop.urls')),
    path('sanitaryworkerswelfare/',include('sanitary.urls')),
    path('orphanwelfare/', include('orphan.urls')),
    path('naturaldisasterservices/', include('naturaldisaster.urls')),
    path('villagedevelopment/',include('villagedev.urls')),
    path('announcements/', include('announcements.urls')),
    path('about/', include('about.urls')),
    path('members/', include('members.urls')),
    path('donate/', include('donate.urls')),
    path('volunteer/', include('volunteer.urls')),
    path('others/', include('others.urls')),
    path('contact/', include('contact.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)