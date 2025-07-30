from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from village.models import Village
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 

USER_TYPE_CHOICES = [
    ('Farmer', 'Farmer'),
    ('Extentionworker', 'Extentionworker'),
    ('Admin', 'Admin'),
]

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_type = models.CharField(
        _("User Type"),
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='Farmer'
    )
    phone_number = models.CharField(_("Phone Number"), max_length=20, unique=True)
    village = models.ForeignKey(
        Village,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='inhabitants'
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'user_type']

    def __str__(self):
        return self.phone_number