from django.db import models

class Refund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    payment_id = models.ForeignKey('payment.Payment', on_delete=models.CASCADE)
    farmer_id = models.ForeignKey('farmer.farmer', on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=50)
    training_schedule_id = models.ForeignKey('schedules.Schedules', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Refund {self.refund_id} - Status: {self.status}"