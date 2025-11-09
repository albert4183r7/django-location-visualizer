from django.contrib import admin
from .models import LocationPoint

@admin.register(LocationPoint)
class LocationPointAdmin(admin.ModelAdmin):
    """
    Admin configuration for LocationPoint model.
    Allows for easy viewing and filtering in the Django admin panel.
    """
    list_display = ('product_id', 'latitude', 'longitude', 'timeStamp', 'iot_gateway_id')
    list_filter = ('product_id', 'iot_gateway_id')
    search_fields = ('product_id', 'timeStamp')