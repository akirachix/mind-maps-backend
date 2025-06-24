# from django.db import models

# # Create your models here.
# class Farmer(models.Model):
#     full_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    village = models.ForeignKey('village.Village', on_delete=models.CASCADE)

    def __str__(self):
        return self.name