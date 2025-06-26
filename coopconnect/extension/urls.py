from django.urls import path
from .views import ExtensionListCreateAPIView, ExtensionDetailAPIView

urlpatterns = [
    path('', ExtensionListCreateAPIView.as_view(), name='refunds-list-create'),  # List and Create
    path('<int:pk>/', ExtensionDetailAPIView.as_view(), name='extension-detail'),  # Retrieve, Update, Delete
]
