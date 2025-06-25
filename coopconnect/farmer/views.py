
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from farmer.models import Farmer
from .serializers import FarmerSerializer

class FarmerListCreateAPIView(ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
