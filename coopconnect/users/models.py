from django.db import models
from village.models import Village

class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=128, null=True)
class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='extensionworker_farmer')
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.full_name
        
class ExtensionWorker(models.Model):
    name = models.CharField(max_length=100)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='users_farmer')
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=26)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name