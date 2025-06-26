from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ExtensionWorker
from .serializers import ExtensionWorkerSerializer
from rest_framework import permissions

# View to list and create extensions
class ExtensionListCreateAPIView(ListCreateAPIView):
    queryset = ExtensionWorker.objects.all()
    serializer_class = ExtensionWorkerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed

# View to retrieve, update, or delete a specific extension
class ExtensionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExtensionWorker.objects.all()
    serializer_class = ExtensionWorkerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed
