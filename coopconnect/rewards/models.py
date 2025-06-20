from django.db import models

# Create your models here.
class Rewards(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    farmer_points = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)