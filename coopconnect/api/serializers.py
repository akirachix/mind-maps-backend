
from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password


from users.models import User 
from trainings.models import Training
from schedules.models import Schedule
from rewards.models import Reward
from village.models import Village
from refunds.models import Refund
from attendance.models import Attendance
from payment.models import Payment



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'} 
    )
    email = serializers.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with that email address already exists.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
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
        read_only_fields = ['id', 'user', 'training', 'created_at', 'updated_at', 'payment_date']


    