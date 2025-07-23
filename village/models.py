from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=100, unique=True)
    village_cell = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.name
