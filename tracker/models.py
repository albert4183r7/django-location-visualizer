from django.db import models

class LocationPoint(models.Model):
    """
    Represents a single location point for a tracked product.
    All fields are required.
    """
    product_id = models.CharField(max_length=100, default='', db_index=True)
    
    # --- UPDATED FIELDS ---
    # Fields are required by default.
    # We are removing 'blank=True' and 'null=True'.
    iot_gateway_id = models.CharField(max_length=100)
    timeStamp = models.CharField(max_length=100) # Removed 'null=True'
    # --- END UPDATES ---
    
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        if self.timeStamp:
             return f"{self.product_id} at ({self.latitude}, {self.longitude}) on {self.timeStamp}"
        return f"{self.product_id} at ({self.latitude}, {self.longitude})"