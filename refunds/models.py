from django.db import models
from django.conf import settings


REFUND_STATUS_CHOICES = [
    ('REQUESTED', 'Requested'),
    ('PROCESSING', 'Processing'),
    ('APPROVED', 'Approved'),
    ('REJECTED', 'Rejected'),
    ('COMPLETED', 'Completed'),
]

class Refund(models.Model):
    transaction_code = models.CharField(
        max_length=200,
        unique=True,
        help_text="Reference to the original payment transaction code, if applicable."
    )
    farmer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='refunds_received',
        limit_choices_to={'user_type': 'Farmer'},
        null=True,
        blank=True
    )
    payment_to_refund = models.ForeignKey(
        'payment.Payment',  
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='refund_attempts',
        help_text="Link to the specific payment being refunded, if applicable."
    )
    schedule = models.ForeignKey(
        'schedules.Schedule',  
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='refunds_for_schedule'
    )
    reason = models.TextField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=REFUND_STATUS_CHOICES,
        default='REQUESTED'
    )
   
    requested_at = models.DateTimeField(auto_now_add=True)

    processed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        farmer_identifier = 'N/A'
        if self.farmer:
            farmer_identifier = getattr(self.farmer, 'username', None) or \
                                getattr(self.farmer, 'email', None) or \
                                f"Farmer PK: {self.farmer.pk}"

        amount_display = self.amount if self.amount is not None else 'N/A'
        return f"Refund for {farmer_identifier} ({amount_display}) - Status: {self.get_status_display()}"

    class Meta:
        ordering = ['-requested_at']
        verbose_name = "Refund"
        verbose_name_plural = "Refunds"

