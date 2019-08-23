from django.db import models

# Create your models here.
class Rental(models.Model):
    price = models.IntegerField()
    features_list = models.CharField(max_length=1000)
    bedrooms  = models.IntegerField()
    bathrooms = models.IntegerField()
    time_to_uofa = models.IntegerField()
    utilities = models.CharField(max_length=300)
    url = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    