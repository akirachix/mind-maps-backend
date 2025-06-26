from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from users.models import *
from .serializers import FarmerSerializer, ExtensionWorkerSerializer ,AdminSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
 
class ExtensionWorkerViewSet(viewsets.ModelViewSet):
    queryset = ExtensionWorker.objects.all()
    serializer_class = ExtensionWorkerSerializer
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer    

