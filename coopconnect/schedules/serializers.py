from rest_framework import serializers
from schedules.models import Schedules

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = "__all__"

