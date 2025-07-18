
from django.contrib.auth.models import AbstractUser
from django.db import models
from village.models import Village
from django.utils.translation import gettext_lazy as _

USER_TYPE_CHOICES = [
        ('Farmer', 'Farmer'),
        ('Extentionworker', 'Extentionworker'),
        ('Admin', 'Admin'),
    ]

class User(AbstractUser): 
       
        name = models.CharField(_("Name of User"), blank=True, max_length=255)
        user_type = models.CharField(
            _("User Type"),
            max_length=20,
            choices=USER_TYPE_CHOICES,
            default='Farmer'
        )
        phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True)
        village = models.ForeignKey(
            Village,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='inhabitants'
        )

        def __str__(self):
            return self.username 

