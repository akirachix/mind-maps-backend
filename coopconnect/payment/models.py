from django.db import models
from farmer.models import Farmer
from schedules.models import Schedules

# Create your models here.

class Payment(models.Model):
    farmer_id = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)
    schedule_id = models.ForeignKey('schedules.Schedules', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    transaction_code = models.CharField(max_length=100)
    points_deducted = models.PositiveIntegerField(blank=True,null=True)
    createdat = models.DateTimeField(auto_now_add=True)