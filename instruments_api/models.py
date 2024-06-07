from django.db import models

# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    condition = models.CharField(max_length=32)
    isRented = models.BooleanField(default=False)
    # rentalStart = models.DateTimeField(auto_now_add=True)
    # rentalEnd = models.DateTimeField(auto_now=True)
   
