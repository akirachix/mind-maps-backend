from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from farmer.models import Farmer
from village.models import Village
from cooperativeadmin.models import Admin
from .serializers import FarmerSerializer, VillageSerializer ,AdminSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer    

