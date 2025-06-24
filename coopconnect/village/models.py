# from django.db import models
# from village.models import Village
# class Village(models.Model):
#     village_name = models.CharField(max_length=100)
#     longitude = models.FloatField()
#     latitude = models.FloatField()

#     def __str__(self):
#         return self.village_name
from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name