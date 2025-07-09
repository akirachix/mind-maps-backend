from django.db import models
from village.models import Village
from django.contrib.auth.models import AbstractUser 


USER_TYPE_CHOICES = [
       ('Farmer', 'Farmer'),
       ('Extentionworker', 'Extentionworker'),
       ('Admin','Admin'),
]
    
    
    

class User(models.Model):
    name = models.CharField(max_length=100)
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='users_farmer')
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=26)
    email = models.CharField(max_length=100)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        blank=True,
        null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='designer')

    def __str__(self):
        return self.name


