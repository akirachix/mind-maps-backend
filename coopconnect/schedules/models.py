from django.db import models
from django.conf import settings 



class Training(models.Model): 
    topic = models.CharField(max_length=200) 
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = "Training"
        verbose_name_plural = "Trainings"
        ordering = ['topic']

class Schedule(models.Model):
    village = models.ForeignKey(
        'village.Village', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='schedules'
    )
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField(null=True, blank=True)
    extension_worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='assigned_schedules',
        limit_choices_to={'user_type': 'Extentionworker'} 
    )
    location_details = models.CharField(max_length=255, blank=True, help_text="Specific location if different from village center, e.g., 'Community Hall'")
    max_attendees = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of attendees allowed")
    is_active = models.BooleanField(default=True, help_text="Is the schedule currently active/planned?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        village_name = self.village.name if self.village else "N/A"
        return f"{self.training.topic} on {self.scheduled_date} in {village_name}"

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"
        ordering = ['scheduled_date', 'scheduled_time']
