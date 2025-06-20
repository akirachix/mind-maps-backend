from django.db import models

# Create your models here.
class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)