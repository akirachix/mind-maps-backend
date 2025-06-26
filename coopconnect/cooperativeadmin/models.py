from django.db import models

class Admin(models.Model):
    
    full_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=128, null=True)
# Create your models here.
