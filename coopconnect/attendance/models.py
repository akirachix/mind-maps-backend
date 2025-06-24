# from django.db import models
#     farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
#     schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
#     village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
#     attended_at = models.DateTimeField(auto_now_add=True)
# # Create your models here.

# from schedules.models import Schedules  # Replace with correct app name if needed
# TODO: Uncomment when the schedules app is ready
# from schedules.models import Schedules
...
# schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
# from village.models import Village

# class Attendance(models.Model):
#     farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
#     # schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
#     village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
#     attended_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.farmer_id} - {self.attended_at}"
from django.db import models
from farmer.models import Farmer
from village.models import Village

class Attendance(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
    attended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_id} - {self.attended_at}"