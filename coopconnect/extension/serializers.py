from rest_framework import serializers
from .models import ExtensionWorker

class ExtensionWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionWorker
        fields = '__all__'