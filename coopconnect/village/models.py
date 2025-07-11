from django.db import models
       
class Village(models.Model):

    village_cell= models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.village_name

