from django.db import models

# Create your models here.
class UserDetails(models.Model):
    fname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    height = models.FloatField()
    married = models.BooleanField()