from django.db import models

# Create your models here.
class Product(models.Model):
    
    title   = models.CharField(max_length=120) 
    desc    = models.TextField(blank=True,null=True)
    price   = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=True)
    feature = models.BooleanField(default=True) #null=True, default=True