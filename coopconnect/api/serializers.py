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
    class Meta:
        model = User
        fields = ['id', 'Full name', 'email', 'is_staff', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    name = serializers.CharField(required=True, label="Full name")
    phone_number = serializers.CharField(required=True)
    village = serializers.PrimaryKeyRelatedField(queryset=Village.objects.all(), required=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    class Meta:
        model = User
        fields = ['name', 'password', 'phone_number', 'village', 'user_type']
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("A user with that phone number already exists.")
        return value
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['username'] = validated_data['phone_number']
        user = super().create(validated_data)
        return user
class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
class SchedulesSerializer(serializers.ModelSerializer):
    training_id = serializers.PrimaryKeyRelatedField(
        queryset=Training.objects.all(),
        write_only=True
    )
    training_name = serializers.CharField(source='training.name', read_only=True)
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['id', 'training_name', 'created_at', 'updated_at']
        
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
    user = UserSerializer(read_only=True)
    schedule = SchedulesSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    schedule_id = serializers.PrimaryKeyRelatedField(
        queryset=Schedule.objects.all(), source='schedule', write_only=True
    )
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id', 'user', 'schedule', 'created_at', 'updated_at', 'attended_at']

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class STKPushSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account_reference = serializers.CharField(max_length=100, default="TX12345")
    transaction_desc = serializers.CharField(max_length=255)











