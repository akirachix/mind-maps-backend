from rest_framework import serializers
from schedules.models import Schedules

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
<<<<<<< HEAD
        fields = "__all__"

=======
        fields = '__all__'    
>>>>>>> 637313f7c580ebaf2fada4e6a490309d0853c26b
