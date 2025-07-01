<<<<<<< HEAD:coopconnect/api/serializers.py


from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
=======
from rest_framework import serializers
from refunds.models import Refund

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model=Refund
        fields="__all__"
>>>>>>> develop:coopconnect/refunds/serializers.py
