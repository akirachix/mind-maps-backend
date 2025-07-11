from rest_framework import serializers
from trainings.models import Trainings
from schedules.models import Schedules
from rewards.models import Rewards
from village.models import Village

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

class  VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'        
