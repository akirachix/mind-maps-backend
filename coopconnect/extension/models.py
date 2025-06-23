from django.db import models
from village.models import Village

# Create your models here.
class ExtensionWorker(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=26)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name