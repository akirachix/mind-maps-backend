from rest_framework import serializers
from rewards.models import Rewards

<<<<<<< HEAD
class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = "__all__"
=======
class  RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'
>>>>>>> 637313f7c580ebaf2fada4e6a490309d0853c26b
