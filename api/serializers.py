from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import User, USER_TYPE_CHOICES
from trainings.models import Training
from schedules.models import Schedule
from rewards.models import Reward
from village.models import Village
from refunds.models import Refund
from attendance.models import Attendance
from .daraja import DarajaAPI
from payment.models import Payment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = [
            'id', 'username', 'name', 'email', 'password',
            'phone_number', 'village', 'user_type',
            'is_staff', 'is_active', 'date_joined'
        ]
        read_only_fields = ['id', 'username', 'is_staff', 'is_active', 'date_joined']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if 'username' not in validated_data or not validated_data['username']:
            validated_data['username'] = validated_data.get('phone_number')
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class SchedulesSerializer(serializers.ModelSerializer):
    training_name = serializers.CharField(source='training.name', read_only=True)
    class Meta:
        model = Schedule
        fields = '__all__'
        
class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'requested_at', 'processed_at']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id', 'farmer', 'schedule', 'created_at', 'updated_at', 'attended_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['id', 'farmer', 'created_at', 'updated_at']

class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_reference = serializers.CharField(max_length=100, default="TX12345")
    transaction_desc = serializers.CharField(max_length=255)











