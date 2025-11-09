from django.db import models

class Location(models.Model):
    id_product = models.CharField(max_length=100,default='')
    iot_gateway_id = models.CharField(max_length=100)
    timeStamp = models.CharField(max_length=100,null=True)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
