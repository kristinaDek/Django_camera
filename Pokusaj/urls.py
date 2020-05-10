"""Pokusaj URL Configuration

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
from django.conf.urls import url,include

from Pokusaj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('error_image/', views.errorImg),
    path('create_dataset/', views.create_dataset),
    path('trainer/', views.trainer),
    path('eigen_train/', views.eigenTrain),
    path('detect/', views.detect),
    path('detect_image/', views.detectImage),

    path('records/', include('records.urls')),

    url(r'^$', views.index),
    url(r'^error_image$', views.errorImg),
    url(r'^create_dataset$', views.create_dataset),
    url(r'^trainer$', views.trainer),
    url(r'^eigen_train$', views.eigenTrain),
    url(r'^detect$', views.detect),
    url(r'^detect_image$', views.detectImage),
    url(r'^admin/', admin.site.urls),
    url(r'^records/', include('records.urls')),
]
