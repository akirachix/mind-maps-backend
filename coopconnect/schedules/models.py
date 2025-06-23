from django.db import models
from trainings.models import Trainings
from extension.models import ExtensionWorker

class Schedules(models.Model):
    training = models.ForeignKey('trainings.Trainings', on_delete=models.CASCADE)
    village = models.ForeignKey('village.Village', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateField()
    extensionworker = models.ForeignKey('extension.ExtensionWorker', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.topic} ({self.date})"