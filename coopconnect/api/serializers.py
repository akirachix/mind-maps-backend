from rest_framework import serializers
from trainings.models import Trainings
from schedules.models import Schedules
from rewards.models import Rewards

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = "__all__"

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = "__all__"

class  RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'
