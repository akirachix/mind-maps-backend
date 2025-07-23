from django.db import models
from django.conf import settings 
from schedules.models import Schedule

PAYMENT_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('COMPLETED', 'Completed'),
    ('REFUNDED', 'Refunded'),
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
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
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
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        farmer_identifier = str(self.farmer) if self.farmer else 'N/A'
        schedule_identifier = str(self.schedule) if self.schedule else 'N/A'
        amount_display = self.amount if self.amount is not None else 'N/A'
        return f"Payment ({amount_display}) by {farmer_identifier} for Schedule ({schedule_identifier}) - {self.get_status_display()}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"