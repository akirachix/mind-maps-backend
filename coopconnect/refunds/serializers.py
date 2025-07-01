from rest_framework import serializers
from refunds.models import Refund

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model=Refund
        fields="__all__"