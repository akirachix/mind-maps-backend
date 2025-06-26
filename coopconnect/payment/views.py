from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import permissions

# View to list and create payments
class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed

# View to retrieve, update, or delete a specific payment
class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed
