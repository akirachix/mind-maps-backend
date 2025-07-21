from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from refunds.models import Refund
from trainings.models import Training
from users.models import User
from rewards.models import Reward
from schedules.models import Schedule
from village.models import Village
from payment.models import Payment
from attendance.models import Attendance
from .daraja import DarajaAPI
from .serializers import (
    STKPushSerializer,
    TrainingsSerializer,
    SchedulesSerializer,
    RewardsSerializer,
    VillageSerializer,
    UserSerializer,
    UserRegistrationSerializer,
    RefundSerializer,
    AttendanceSerializer,
    PaymentSerializer,
)
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "User registered successfully."},
            status=status.HTTP_201_CREATED,
        )
class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingsSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Training.objects.all()
        return Training.objects.none()
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save()
class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = SchedulesSerializer
class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardsSerializer
class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [permissions.AllowAny]
        elif self.action in [
            "list",
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ]:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Refund.objects.all()
        return Refund.objects.none()
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Payment.objects.all()
        return Payment.objects.none()
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
class STKPushView(APIView):
    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            daraja = DarajaAPI()
            try:
                response = daraja.stk_push(
                    phone_number=data["phone_number"],
                    amount=data["amount"],
                    account_reference=data["account_reference"],
                    transaction_desc=data["transaction_desc"],
                )
                return Response(response, status=status.HTTP_200_OK)
            except Exception as e:
                # Return the error details for debugging
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def daraja_callback(request):
    print("Daraja Callback Data:", request.data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})










