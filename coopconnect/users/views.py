

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import AdminSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
