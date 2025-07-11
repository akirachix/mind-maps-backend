from django.db import models
from attendance.models import Attendance
from farmer.models import Farmer

# Create your models here.
class Rewards(models.Model):
    farmer_id = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)
    attendance_id = models.ForeignKey('attendance.Attendance', on_delete=models.CASCADE)
    farmer_points = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    