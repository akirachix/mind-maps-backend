from django.urls import path
from .views import PaymentListCreateAPIView, PaymentDetailAPIView

urlpatterns = [
    path('', PaymentListCreateAPIView.as_view(), name='payment-list-create'),  # List and Create
    path('<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),  # Retrieve, Update, Delete
]
