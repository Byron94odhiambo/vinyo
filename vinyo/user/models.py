import email
from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    email = models.CharField(max_length=100)
    active = models.BooleanField()
    accounts =models.CharField(max_length=200)
    tier= models.CharField(max_length=100)
    
    
    
    


