from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)  # Allow null and blank

    def __str__(self):
        return self.name
