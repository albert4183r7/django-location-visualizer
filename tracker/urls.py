from django.urls import path
from . import views

# This creates a namespace for the app, e.g., 'tracker:map_view'
app_name = 'tracker'

urlpatterns = [
    # Path for the main map view
    path('', views.track_map_view, name='map_view'),
]