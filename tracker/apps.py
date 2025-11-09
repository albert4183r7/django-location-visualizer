from django.apps import AppConfig


class TrackerConfig(AppConfig):  # Renamed from MapApiConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'  # Renamed from 'map_api'