from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from payment.models import Payment

from village.models import Village

from .serializers import PaymentSerializer


from .serializers import  VillageSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer


