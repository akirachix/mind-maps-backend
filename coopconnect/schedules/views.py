from django.shortcuts import render

from rest_framework import viewsets
from schedules.models import Schedules
from .serializers import SchedulesSerializer
class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer

