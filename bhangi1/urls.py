"""bhangi1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from gad1 import views
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
    url(r'^gad1/', include('gad1.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    # garegeeaish
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/registration/', views.registration, name='registration'),
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),

]
#success_url = reverse_lazy('/gad1/page1'),