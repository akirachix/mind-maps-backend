from rest_framework import serializers
from rewards.models import Rewards

class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = "__all__"