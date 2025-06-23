from django.db import models
from farmer.models import Farmer
from schedules.models import Schedules
from village.models import Village

class Attendance(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
    attended_at = models.DateTimeField(auto_now_add=True)