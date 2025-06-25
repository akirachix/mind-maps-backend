from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from refunds.models import Refund
from .serializers import RefundSerializer

class RefundViewSet(viewsets.ModelViewSet):
    queryset=Refund.objects.all()
    serializer_class=RefundSerializer
