"""
location_visualizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the tracker app's URLs
    path('tracker/', include('tracker.urls')),
    # Redirect the root URL to the tracker app
    path('', RedirectView.as_view(url='/tracker/', permanent=True)),
]