
from django.db import models
from django.conf import settings 
from schedules.models import Schedule
from village.models import Village


class Attendance(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='attendances',
        limit_choices_to={'user_type': 'Farmer'},
        null=True, 
        blank=True 
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        null=True, 
        blank=True  
    )
    village = models.ForeignKey(
        Village,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True  
    )
    attended_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=500, blank=True, null=True) 

    def __str__(self):
        farmer_name = self.farmer.username if self.farmer and hasattr(self.farmer, 'username') else 'N/A'
        schedule_info = 'N/A'
        if self.schedule and hasattr(self.schedule, 'training') and self.schedule.training and hasattr(self.schedule.training, 'topic'):
            schedule_info = self.schedule.training.topic
        return f"Attendance for {farmer_name} at {schedule_info} on {self.attended_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-attended_at']
        verbose_name = "Attendance Record"
        verbose_name_plural = "Attendance Records"

