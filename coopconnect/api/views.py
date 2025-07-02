
# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets
from trainings.models import Trainings
from .serializers import TrainingsSerializer
class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer


from rest_framework import viewsets
from schedules.models import Schedules
from .serializers import SchedulesSerializer
class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer



from rest_framework import viewsets
from rewards.models import Rewards
from .serializers import RewardsSerializer
class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer


