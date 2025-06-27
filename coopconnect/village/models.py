from django.db import models
class Village(models.Model):
    village_name = models.CharField(max_length=100)
    longtitude  = models.FloatField()
    latitude = models.FloatField()
    def __str__(self):
        return self.village_name
# Create your models here.
