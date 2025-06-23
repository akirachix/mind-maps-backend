from django.db import models
from village.models import Village

# Create your models here.
class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name