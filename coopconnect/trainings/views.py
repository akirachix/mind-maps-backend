from django.shortcuts import render

from rest_framework import viewsets
from trainings.models import Trainings
from .serializers import TrainingsSerializer
class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer

