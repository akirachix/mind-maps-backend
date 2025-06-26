from rest_framework import serializers
from users.models import *

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class ExtensionWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionWorker
        fields = '__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UserUnionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    email = serializers.EmailField(allow_null=True)
    phone_number = serializers.CharField(allow_null=True)
    password = serializers.CharField()
    user_type = serializers.CharField()

