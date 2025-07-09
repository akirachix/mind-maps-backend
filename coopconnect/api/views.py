
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Trainings,Rewards,Schedules,Village
from .serializers import TrainingsSerializer,SchedulesSerializer,RewardsSerializer,VillageSerializer

class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer


class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer


class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer

 
class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
   


