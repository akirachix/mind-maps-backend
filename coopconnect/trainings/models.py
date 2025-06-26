from django.db import models




class Trainings(models.Model):
    topic = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2)