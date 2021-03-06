"""movies_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from django.contrib.auth.decorators import login_required
from django.contrib.auth import urls as auth_urls

from rest_framework.routers import DefaultRouter

from .views import IndexView, AddMovieView
from movies import viewsets



router = DefaultRouter()
router.register(r'movies', viewsets.MovieViewSet)

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    url(r'^add/', AddMovieView.as_view(), name='addMovie'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^', include(auth_urls)),
]
