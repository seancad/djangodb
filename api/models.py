from django.db import models

# Create your models here.
class Rental(models.Model):
    monthly_price = models.IntegerField()