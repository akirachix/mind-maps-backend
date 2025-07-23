from django.db import models
from django.conf import settings 
from users.models import User
from django.db import models
from django.conf import settings 
from users.models import User
from trainings.models import Training

class Schedule(models.Model):
    training = models.ForeignKey(
       'trainings.Training', 
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    village = models.ForeignKey(
        'village.Village', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='schedules'
    )
    extension_worker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='assigned_schedules',
        limit_choices_to={'user_type': 'Extentionworker'} 
    )
    max_attendees = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of attendees allowed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

