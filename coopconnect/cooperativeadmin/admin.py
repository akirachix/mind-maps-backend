# cooperativeadmin/admin.py

from django.contrib import admin
from .models import Admin  # This imports the Admin model from your own app

admin.site.register(Admin)