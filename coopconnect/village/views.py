from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from village.models import Village

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer