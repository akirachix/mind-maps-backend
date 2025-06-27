from rest_framework import serializers 

from payment.models import Payment

from village.models import Village



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'




class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
        