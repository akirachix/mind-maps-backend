from django.db import models

class Refund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    transaction_code = models.CharField(max_length=200)
    farmer_id = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=50)
    training_schedule_id = models.ForeignKey('schedules.Schedules', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Refund {self.refund_id} - Status: {self.status}"