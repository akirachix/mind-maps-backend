from django.db import models
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    village_id = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
    attended_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
