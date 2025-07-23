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
    RefundSerializer,
    AttendanceSerializer,
    PaymentSerializer,
)

class TrainingsViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingsSerializer
  
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
    
    
class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

     
   
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.utils import timezone
import datetime

class STKPushView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

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
                checkout_request_id = response.get('CheckoutRequestID', None)
                if checkout_request_id:
                    Payment.objects.create(
                        phone_number=data['phone_number'],
                        amount=data['amount'],
                        transaction_code=checkout_request_id,
                        status='PENDING'
                    )
                return Response(response, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def daraja_callback(request):
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)
    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']
        payment = Payment.objects.get(transaction_code=checkout_request_id)
        payment.status = 'COMPLETED' if result_code == 0 else 'FAILED'
        payment.result_description = result_desc
        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}
            payment.mpesa_receipt_number = item_dict.get('MpesaReceiptNumber')
            trans_date_str = str(item_dict.get('TransactionDate'))
            trans_date = datetime.datetime.strptime(trans_date_str, '%Y%m%d%H%M%S')
            payment.transaction_date = timezone.make_aware(trans_date, timezone.get_current_timezone())
            payment.amount = item_dict.get('Amount')
            payment.phone_number = item_dict.get('PhoneNumber')
        payment.save()
    except Payment.DoesNotExist:
        print(f"Payment with CheckoutRequestID {checkout_request_id} not found.")
    except Exception as e:
        print(f"Error processing Daraja callback: {e}")
    return










