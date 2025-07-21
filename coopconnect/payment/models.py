from django.db import models
from django.conf import settings 
from schedules.models import Schedule


PAYMENT_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('COMPLETED', 'Completed'),
    ('FAILED', 'Failed'),
    ('REFUNDED', 'Refunded'),
]

PAYMENT_METHOD_CHOICES = [
    ('MOBILE_MONEY', 'Mobile Money'),
    ('POINTS', 'Points'), 
]

class Payment(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE, 
        related_name='payments',
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
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        blank=True, 
        null=True   
    )
    status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default='PENDING'
    )
    transaction_code = models.CharField( 
        max_length=100,
        unique=True, 
        blank=True,
        null=True 
    )
    points_deducted = models.PositiveIntegerField(
        default=0, 
        help_text="Points deducted if payment method was 'Points'" 
    )
    createdat = models.DateTimeField(
        auto_now_add=True,
    )
  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        farmer_identifier = 'N/A'
        if self.farmer:
            farmer_identifier = self.farmer.username if hasattr(self.farmer, 'username') else str(self.farmer.pk)

        schedule_identifier = 'N/A'
        if self.schedule and hasattr(self.schedule, 'training') and self.schedule.training and hasattr(self.schedule.training, 'topic'):
            schedule_identifier = self.schedule.training.topic
        elif self.schedule:
            schedule_identifier = str(self.schedule.pk)

        amount_display = self.amount if self.amount is not None else 'N/A'
        return f"Payment ({amount_display}) by {farmer_identifier} for Schedule ({schedule_identifier}) - {self.get_status_display()}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

