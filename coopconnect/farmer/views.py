from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from farmer.models import Farmer
from .serializers import FarmerSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
