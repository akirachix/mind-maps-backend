from django.db import models

class Training(models.Model):
    topic = models.CharField(max_length=255)
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
