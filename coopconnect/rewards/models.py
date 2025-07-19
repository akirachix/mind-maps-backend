from django.db import models
from django.conf import settings
from attendance.models import Attendance

class Reward(models.Model): 
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rewards_received',
        limit_choices_to={'user_type': 'Farmer'}
    )
    attendance = models.OneToOneField( 
        'attendance.Attendance',
        on_delete=models.CASCADE,
        related_name='reward', 
        help_text="The attendance record that earned this reward."
    )
    points_awarded = models.PositiveIntegerField(
        help_text="Number of points awarded for this specific attendance."
    )
    awarded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the reward was created."
    )


    def __str__(self):
        return f"Reward of {self.points_awarded} points for {self.farmer.username if self.farmer else 'N/A'} (Attendance: {self.attendance_id})"

    class Meta:
        ordering = ['-awarded_at']
        verbose_name = "Reward"
        verbose_name_plural = "Rewards"
        unique_together = [['farmer', 'attendance']]



class FarmerPointBalance(models.Model):
    farmer = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='point_balance',
        limit_choices_to={'user_type': 'Farmer'}
    )
    total_points = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.farmer.username if self.farmer else 'N/A'} - Total Points: {self.total_points}"

    class Meta:
        verbose_name = "Farmer Point Balance"
        verbose_name_plural = "Farmer Point Balances"

